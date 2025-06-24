import asyncio
from dataclasses import dataclass
from pydantic import BaseModel
from agents import Agent, Runner
from config import config

@dataclass
class CalendarEvent():
    name: str
    date: str
    participants: list[str]
    location_room: int

agent2 = Agent(
    name="English Assistant",
    instructions="You are english expert",
)
agent3 = Agent(
    name="Math Assistant",
    instructions="You are math expert",
)
agent = Agent(
    name="Calendar extractor",
    instructions="Extract calendar events from text",
    handoffs=[agent2, agent3],
    output_type=CalendarEvent,
)

async def main():
    result = await Runner.run(
        agent,
        "I have a meeting with Hamza, Usman, Abubakar, and Ali on 2025-06-01 at 10:00 AM at Governer house in room no 39",
        run_config=config
    )
    # print(result.final_output)

asyncio.run(main())