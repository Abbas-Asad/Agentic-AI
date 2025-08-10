from agents import Agent, Runner, function_tool
from agentsdk_gemini_adapter import config
from rich import print
from dataclasses import dataclass

@function_tool
def add(a: int, b: int) -> int:
    """
    This is a tool that adds two numbers
    Args:
        a: First number
        b: Second number
    Returns:
        Sum of two numbers
    """
    return a + b

@function_tool
def subtract(a: int, b: int) -> int:
    """
    This is a tool that subtracts two numbers
    Args:
        a: First number
        b: Second number
    Returns:
        Result of two numbers subtraction
    """
    return a - b

english_agent = Agent(
    name="English agent", 
    instructions="You are english assistant"
)

# @dataclass
# class OutputSchema:
#     answer: str
#     reason: str
#     verified: int

agent = Agent(
    name="Assistant", 
    instructions="You are a helpful assistant. Handoff to english agent if the user's query is related to english. Use tool when query is related to math.",
    tools=[add, subtract],
    handoffs=[english_agent],
    # output_type=OutputSchema
)

result = Runner.run_sync(
    agent, 
    "What is pronoun? Answer in a line.", 
    run_config=config
)

print("\nfinal_output:", result.final_output)