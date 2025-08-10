import asyncio
from openai.types.responses import ResponseTextDeltaEvent
from agents import Agent, Runner
from config import config
# from pydantic import BaseModel, EmailStr

agent = Agent(name = "assistant", instructions = "You are a helpful assistant")

async def main():
    result = Runner.run_streamed(agent, input="Please tell me 5 jokes.", run_config= config)
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)

asyncio.run(main())