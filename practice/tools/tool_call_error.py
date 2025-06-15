from config import config
from agents import Agent, Runner, function_tool, enable_verbose_stdout_logging, RunContextWrapper

# enable_verbose_stdout_logging()

def custom_failure_message(
        context: RunContextWrapper[None], error: Exception
) -> str:
    return f"Custom error message: {str(error)}\nRepr: {repr(error)}, Type: {type(error)}, Args: {error.args}"

@function_tool(failure_error_function=custom_failure_message,)
# def buggy_calculator(a: float, b: float) -> float:
#     """Deliberately buggy calculator that divides by zero if b is 0"""
#     # return a / b  # ⚠️ Will raise ZeroDivisionError if b == 0
#     raise ZeroDivisionError("This is a ZeroDivisionError")
def fetch_weather_data():
    """This tool is responsible for fetching weather data"""
    raise ValueError("Not found")
    # return "The weather is sunny"

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant.",
    tools=[fetch_weather_data]
)

# 🔥 This will raise division by zero, triggering default_tool_error_function
user_input = "What is the weather in Karachi?"

result = Runner.run_sync(agent, user_input, run_config=config)

print("=============================")

def default_tool_error_function(error: Exception) -> str:
    """The default tool error function, which just returns a generic error message."""
    raise ValueError("Not found")
print(repr(ValueError))
# print(fetch_weather_data)
# print(result.final_output)
