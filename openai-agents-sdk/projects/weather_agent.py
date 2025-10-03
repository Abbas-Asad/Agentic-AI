import os
import chainlit as cl
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

gemini_api_key = os.getenv("GEMINI_API_KEY")
#  3 heezain about type hints        aur pydantic
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

weather_instructions = """
You are a weather information assistant who helps users understand weather patterns and phenomena.

YOUR EXPERTISE:
- Explaining weather concepts and terminology
- Describing how different weather systems work
- Answering questions about climate and seasonal patterns
- Explaining the science behind weather events

LIMITATIONS:
- You cannot provide real-time weather forecasts for specific locations
- You don't have access to current weather data
- You should not make predictions about future weather events

STYLE:
- Use clear, accessible language that non-meteorologists can understand
- Include interesting weather facts when relevant
- Be enthusiastic about meteorology and climate science
"""

weather_agent: Agent = Agent( name= "Weather Assistant" , instructions= weather_instructions )

@cl.on_message
async def handle_message(message: cl.Message):
    # Otherwise run LLM
    result = await Runner.run(
        weather_agent,
        input=message.content,
        run_config=config,
    )
    await cl.Message(content=result.final_output).send()
    
