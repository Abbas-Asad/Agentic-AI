from agents import Agent, Runner, function_tool, ModelSettings
from agentsdk_gemini_adapter import config


agent = Agent(
    name="Assistant", 
    instructions="You are a helpful assistant.",
    model_settings=ModelSettings(truncation="k")  
)

input = "Who is the founder"
result = Runner.run_sync(agent, input, run_config=config)
print(result.final_output)
















# from agents import Agent, Runner, function_tool, ModelSettings
# from agentsdk_gemini_adapter import config

# # @function_tool
# # def fetch_weather():
# #     """This will fetch the weather"""
# #     return "The weather in Pakistan is sunny."

# # @function_tool
# # def fetch_currency():
# #     """This will fetch the currency"""
# #     return "The currency of Pakistan is rupee"

# # @function_tool
# # def fetch_population():
# #     """This will fetch the population"""
# #     return "The population of Pakistan is about 240 million."

# # @function_tool
# # def fetch_capital():
# #     """This will fetch the capital city"""
# #     return "The capital of Pakistan is Islamabad."

# # @function_tool
# # def fetch_language():
# #     """This will fetch the official language"""
# #     return "The official language of Pakistan is Urdu."

# # @function_tool
# # def fetch_flag_color():
# #     """This will fetch the flag color"""
# #     return "The flag of Pakistan is green and white."

# # @function_tool
# # def fetch_national_animal():
# #     """This will fetch the national animal"""
# #     return "The national animal of Pakistan is the Markhor."

# # @function_tool
# # def fetch_national_sport():
# #     """This will fetch the national sport"""
# #     return "The national sport of Pakistan is field hockey."

# agent = Agent(
#     name="Assistant", 
#     instructions="You are a helpful assistant.",
#     # tools=[fetch_weather, fetch_currency, fetch_population, fetch_capital, fetch_language, fetch_flag_color, fetch_national_animal, fetch_national_sport],
#     model_settings=ModelSettings(parallel_tool_calls=False)  # Agar supported ho
# )

# input = "What is the weather, currency, population, capital, official language, flag color, national animal, and national sport of Pakistan?"
# result = Runner.run_sync(agent, input, run_config=config)
# print(result.final_output)
