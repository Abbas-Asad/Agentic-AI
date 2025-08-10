from agents import Agent, Runner, function_tool
from agentsdk_gemini_adapter import config
from rich import print

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

@function_tool
def define_noun() -> str:
    """This will define noun"""
    return "Noun is any name."

@function_tool
def define_pronoun() -> str:
    """This will define pronoun"""
    return "Pronoun is which is used to replace noun."

english_agent = Agent(
    name="English agent", 
    instructions="You are english assistant. Answer user queries.",
    # tools=[define_noun, define_pronoun]
)

agent = Agent(
    name="Assistant", 
    instructions="You are a helpful assistant. Handoff to english agent if the user's query is related to english.",
    # tools=[add, subtract],
    handoffs=[english_agent],
)

result = Runner.run_sync(
    agent, 
    "What is noun? Answer in a line.", 
    run_config=config
)

print("\nfinal_output:", result.final_output)