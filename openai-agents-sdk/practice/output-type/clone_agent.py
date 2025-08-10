# import asyncio
# from dataclasses import dataclass
# from pydantic import BaseModel
from agents import Agent, Runner
from config import config

english_agent = Agent(
    name="english agent",
    instructions="You are English expert",
)

# agent = english_agent.clone()


result = Runner.run_sync(
    english_agent,
    "what is calculus?",
    run_config=config
)

print(result.final_output)
    # print(f"Result is: \n{type(result.final_output.location_room)}\n")
