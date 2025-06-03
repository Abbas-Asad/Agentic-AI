# RunItemStreamEvent & AgentUpdatedStreamEvent

import asyncio
import random
from config import config
from agents import Agent, Runner, function_tool, ItemHelpers

@function_tool
def how_many_jokes():
    """
    This is the number of joke
    """
    return random.randint(1, 10)

agent= Agent(
    name="Joker", 
    instructions="First call the `how_many_jokes` tool, then tell that many jokes.",
    tools=[how_many_jokes],
)

async def main():
    result = Runner.run_streamed(
        agent,
        input="Hello",
        run_config=config
    )
    
    async for event in result.stream_events():
        if event.type == "raw_response_event":
            continue
        elif event.type == "agent_updated_stream_event":
            # print(f"Current agent: {result.current_agent.name}") # Current agent
            print(f"Updated agent: {event.new_agent.name}")
            continue
        elif event.type == "run_item_stream_event":
            if event.item.type == "tool_call_item":
                print("Tool was called")
            elif event.item.type == "tool_call_output_item":
                print(f"Tool output: {event.item.output}")
            elif event.item.type == "message_output_item":
                print(f"Message: {ItemHelpers.text_message_output(event.item)}")

asyncio.run(main())