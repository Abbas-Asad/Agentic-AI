import os
import chainlit as cl
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

openrouter_api_key = os.getenv("OPENROUTER_API_KEY")

# ✅ Setup OpenRouter as OpenAI-compatible client
external_client = AsyncOpenAI(
    api_key=openrouter_api_key,
    base_url="https://openrouter.ai/api/v1",
)

# ✅ Set the model you want to use (you can try "mistralai/mixtral-8x7b" or "openai/gpt-4")
model = OpenAIChatCompletionsModel(
    model="deepseek/deepseek-chat:free",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

research_instructions = """You are a research assistant that helps users find and summarize information.
1. Search the web for relevant, up-to-date information
2. Synthesize the information into a clear, concise summary
3. Structure your response with headings and bullet points when appropriate
4. Always cite your sources at the end of your response

If the information might be time-sensitive or rapidly changing, mention when the search was performed.
"""

# 🧠 Agent Setup
research_agent: Agent = Agent(
    name="Research Assistant",
    instructions=research_instructions
)

# 🚀 Handle incoming messages
@cl.on_message
async def handle_message(message: cl.Message):
    result = await Runner.run(
        research_agent,
        input=message.content,
        run_config=config,
    )
    await cl.Message(content=result.final_output).send()



