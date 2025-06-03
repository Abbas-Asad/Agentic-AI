from agents import Agent, Runner
from config import config

english_agent = Agent(name="english agent", instructions="You have to help in english grammar related queries. your name is abbas")
agent = english_agent.clone(
    instructions="You have to help in english grammar related queries. your name is asad"
)

result = Runner.run_sync(agent, "what are your expertise? tell me in one line and also tell your name", run_config=config)
print(result.final_output)
# print(dir(agent))
# print(agent)