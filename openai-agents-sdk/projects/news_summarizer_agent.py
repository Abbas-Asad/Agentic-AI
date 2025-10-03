import chainlit as cl
from agents import Agent, Runner, function_tool
from duckduckgo_search import DDGS
from datetime import datetime
from typing import List, Dict, Any
from config import config

# DuckDuckGo Search Tool
@function_tool
def duckduckgo_news(query: str = "latest news", max_results: int = 5) -> List[Dict[str, Any]]:
    """Search for the latest news headlines."""
    try:
        with DDGS() as ddgs:
            return list(ddgs.news(query, max_results=max_results))
    except Exception as e:
        return [{"error": f"Search failed: {str(e)}"}]

# Agent Instructions
news_instructions = f"""
You are a professional News Summarizer Agent. Your task is to:
1. Use the `duckduckgo_news` tool to fetch the top news headlines.
2. Summarize the top 3–5 stories in clear bullet points.
3. Categorize them under sections like Tech, Politics, Sports, etc. if possible.
4. Include the date/time like this: *As of {datetime.now().strftime('%B %d, %Y at %I:%M %p')}*
5. Keep the summary short, objective, and helpful.

Always stay neutral and focus on summarizing the **facts**, not opinions.
"""

# News Agent
news_agent = Agent(
    name="News Summarizer",
    instructions=news_instructions,
    tools=[duckduckgo_news],
)


# First Message When Chat Starts
@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history", [])
    await cl.Message(content=
                        "**Welcome to the News Summarizer Assistant 📰**\n\n"
                        "I'm here to help you quickly understand the key points from any news article. "
                        "Just give me the topic or type 'latest news', and I'll take care of the rest."
                     ).send()

# Handle user messages with session history
@cl.on_message
async def handle_message(message: cl.Message):
    history = cl.user_session.get("history")

    # Standard Interface [{"role": "user", "content": "Hello!"}, {"role": "assistant", "content": "..."}]
    history.append({"role": "user", "content": message.content})
    
    result = await Runner.run(
        news_agent,
        input=history,
        run_config=config,
    )

    history.append({"role": "assistant", "content": result.final_output})
    cl.user_session.set("history", history)
    await cl.Message(content=result.final_output).send()
