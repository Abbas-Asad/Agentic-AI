from config import config
from agents import Agent, Runner, function_tool, enable_verbose_stdout_logging

enable_verbose_stdout_logging()

@function_tool
def calculator(operation: str, a: float, b: float) -> float:
    """A calculator tool that performs basic arithmetic operations between two numbers.
    
    This tool can perform four basic arithmetic operations: addition, subtraction, multiplication, and division.
    It takes two numbers and an operation type as input and returns the result of the calculation.
    
    Args:
        operation (str): The arithmetic operation to perform. Must be one of: "add", "subtract", "multiply", "divide"
        a (float): The first number in the calculation
        b (float): The second number in the calculation
    
    Returns:
        float: The result of the arithmetic operation. Returns an error message if:
            - The operation is invalid
            - Division by zero is attempted
    
    Example:
        calculator("add", 5, 3) returns 8
        calculator("multiply", 4, 2) returns 8
    """
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b if b != 0 else "Error: Division by zero"
    else:
        return "Error: Invalid operation"
    
agent = Agent(
  name="LoopingBot",
  tools=[calculator],
  reset_tool_choice=False,
  instructions="Regardless of the input, always call the calculator tool. Do not answer, explain, or apologize. Always use calculator with dummy inputs like 1+1. Do only this",
)

input = "What is the capital of Pakistan?"
result = Runner.run_sync(agent, input, run_config=config, max_turns=3)
print(result.final_output)
