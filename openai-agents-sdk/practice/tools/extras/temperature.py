from agents import Agent, Runner, ModelSettings
from config import config

agent = Agent(name="Assistant", instructions="You are a helpful assistant")
# model_settings=ModelSettings(temperature=0.0)
# We have set model globally in config.py so we can't set temperature here but the point is whenever temperature is 0 (0.0-1.0) so the output will be fix every time

result = Runner.run_sync(agent, "What is programming? (Answer in 1 line)", run_config=config)
print(result.final_output)