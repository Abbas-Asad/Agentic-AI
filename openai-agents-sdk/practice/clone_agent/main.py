from agents import Agent, Runner
from config import config

math_agent = Agent(name="Assistant", instructions="You are a maths expert assistant.")

english_agent = math_agent.clone(
    instructions="You are an english expert assistant."
)

result = Runner.run_sync(english_agent, "Hello", run_config=config)
# print(result.final_output)

print("math_agent name: ", math_agent.name)
print("math_agent instructions: ", math_agent.instructions)
print("====================================================")
print("english_agent name: ", english_agent.name)
print("english_agent instructions: ", english_agent.instructions)
