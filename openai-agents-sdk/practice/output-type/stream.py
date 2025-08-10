import asyncio
from config import config
from agents import Agent, Runner
from openai.types.responses import ResponseTextDeltaEvent

agent = Agent(name="Assistant", instructions="You are a helpful assistant")

# This is an async function that can be paused and resumed
async def main():
    result = Runner.run_streamed(agent, "Tell me 5 jokes.", run_config=config)

    # This is an async iterator that yields events as they arrive
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta)

asyncio.run(main())