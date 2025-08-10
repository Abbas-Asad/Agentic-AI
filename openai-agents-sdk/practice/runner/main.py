from agents import Agent, Runner
from agentsdk_gemini_adapter import config
import asyncio

agent = Agent(name="Assistant", instructions="You are a helpful assistant")

async def main():
    result = await Runner.run(agent, "What is noun?", run_config=config)
    print(result.final_output)

asyncio.run(main())