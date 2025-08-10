# from agents import Agent, Runner
# from config import config

# agent = Agent(name = "Agent 1", instructions = "You are a joke assistant.")

# result = Runner.run_sync(agent , input = "Tell me 5 jokes", run_config = config)

# print(result.final_output)

import asyncio
from openai.types.responses import ResponseTextDeltaEvent
from agents import Agent, Runner
from config import config

async def main():
    agent = Agent(
        name="Joker",
        instructions="You are a helpful assistant.",
    )

    result = Runner.run_streamed(agent, input="Please tell me 5 jokes.", run_config = config)
    async for event in result.stream_events():
        if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
            print(event.data.delta, end="", flush=True)


if __name__ == "__main__":
    asyncio.run(main())

# https://www.youtube.com/live/G4NjwWTY2c8?si=eo-EDz_jBqdGD9sg&t=3862