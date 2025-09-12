from agents import Agent, Runner
from agentsdk_gemini_adapter import config


agent = Agent(
    name="Assistant", 
    instructions="You are a helpful assistant."
)

input = "Who is the founder"
result = Runner.run_sync(agent, input, run_config=config)
print(result.final_output)