from agents import Agent, Runner, function_tool, handoff, enable_verbose_stdout_logging
from config import config

enable_verbose_stdout_logging()

# @function_tool
# def fetch_username():
#     """This will return username"""
#     return "Abbas"

# @function_tool
# def fetch_userage():
#     """This will return userage"""
#     return 22

# @function_tool
# def fetch_weather(city):
#     """This will return the weather of the city"""
#     return f"The weather in {city} is sunny."


# agent2 = Agent(
#     name="Math expert", 
#     instructions="You are a math expert", 
# )

# agent3 = Agent(
#     name="Python expert", 
#     instructions="You are a python expert", 
# )

agent = Agent(
    name="Assistant", 
    instructions="You are a helpful assistant.", 
    # handoffs=[agent2, agent3],
    # tools=[fetch_username, fetch_userage, fetch_weather]
)

# input = "What's the weather in Karachi?"
input = "What's is right angle?"
# input = "What's is username."
result = Runner.run_sync(agent, input, )
print(result.final_output)
