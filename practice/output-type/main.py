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

agent = Agent(
    name="Calendar extractor",
    instructions="Extract calendar events from text",
    # instructions="You are a helpful assistant.",
    output_type=CalendarEvent,
)

async def main():
    result = await Runner.run(
        agent,
        "I have a meeting with Hamza, Usman, Abubakar, and Ali on 2025-06-01 at 10:00 AM at Governer house in room no 39",
        # "Hello! My name is Abbas, today's date is 6/4/25 an my location room is Nazimabad flat 123 room 1234",
        run_config=config
    )

    print(f"Result is: \n{result.final_output}\n")
    print(f"location_room type is: \n{type(result.final_output.location_room)}\n")

if __name__ == "__main__":
    asyncio.run(main())