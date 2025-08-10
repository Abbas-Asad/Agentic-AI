from config import config
from agents import Agent, Runner, function_tool


def my_custom_error_handler(error: Exception) -> str:
    """Custom error message"""
    return "Oops! The tool encountered an error. Please try again later."


@function_tool
def failing_tool():
    """This tool will always fail"""
    raise ValueError("This is a test error from the tool")


agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant try to call the tool whatever you have",
    tools=[failing_tool]
)

result = Runner.run_sync(
    agent,
    "Call the failing tool",
    run_config=config
)
print("Final Output:", result.final_output)