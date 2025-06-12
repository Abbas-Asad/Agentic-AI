import requests
import chainlit as cl
from agents import Agent, Runner, function_tool
from openai.types.responses import ResponseTextDeltaEvent
from typing import List, Dict, Any
from duckduckgo_search import DDGS
from datetime import datetime
from config import config 
import asyncio

# DuckDuckGo search tool
@function_tool
def duckduckgo_search(query: str, max_results: int = 5) -> List[Dict[str, Any]]:
    """Search DuckDuckGo for a given query."""
    try:
        with DDGS() as ddgs:
            return list(ddgs.text(query, max_results=max_results))
    except Exception as e:
        return [{"error": f"Search failed: {str(e)}"}]

# API data fetch tool
@function_tool
def fetch_api_data(url: str) -> Dict[str, Any]:
    """Fetch JSON data from an API URL and return the result."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        return {"error": f"Failed to fetch data: {str(e)}"}

# System Prompt
product_data_fetcher_instructions = f"""
You are a professional product detail assistant specialized in helping users extract and understand e-commerce product information.

Your capabilities include:
1. Fetching real-time product data from API URLs provided by the user.
2. Extracting key fields such as:
   - 📌 Product Name or Title
   - 💰 Price (with discount if any)
   - ✅ Availability
   - ⭐ Ratings and Reviews (if present)
3. Using the `fetch_api_data` tool for APIs or falling back to `duckduckgo_search` when only search terms are provided.
4. Comparing multiple product links if more than one is given.
5. Structuring responses using clear **headings**, **bullet points**, or **tables**.
6. Always mention the source (API URL or search link).
7. Clearly mention the timestamp of data retrieval like this: *As of {datetime.now().strftime('%B %d, %Y at %I:%M %p')}*.

🎯 Always answer clearly and concisely like a professional product analyst.
"""

# Create Product Detail Assistant Agent
product_agent: Agent = Agent(
    name="Product Detail Assistant",
    instructions=product_data_fetcher_instructions,
    tools=[fetch_api_data, duckduckgo_search]
)

# First Message When Chat Starts
@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history", [])
    await cl.Message(
        content=(
            "**Product Analysis Assistant 🛍️**\n\n"
            "I'm here to help you explore and compare e-commerce products with ease. You can:\n"
            "- Provide a product API URL to fetch details (name, price, availability, ratings)\n"
            "- Describe a product to search for online using DuckDuckGo\n\n"
            "Simply paste an API link or type a product name, and I'll deliver a professional analysis with the latest data. Let's get shopping! 👇\n"
        )
    ).send()

# Handle incoming messages with streaming
@cl.on_message
async def handle_message(message: cl.Message):
    history = cl.user_session.get("history", [])
    history.append({"role": "user", "content": message.content})

    # Create a Chainlit message for streaming
    msg = cl.Message(content="")
    await msg.send()

    # Run the agent with streaming
    final_output = ""
    async for event in Runner.run_streamed(
        product_agent,
        input=history,
        run_config=config,
    ).stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            delta = event.data.delta
            if delta:  # Ensure delta is not empty
                final_output += delta
                await msg.stream_token(delta)  # Stream the delta to the Chainlit UI

    # Update the history with the final output
    history.append({"role": "assistant", "content": final_output})
    cl.user_session.set("history", history)

    # Finalize the message
    await msg.update()

if __name__ == "__main__":
    asyncio.run(cl.run())