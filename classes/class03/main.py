from agents import Agent, Runner
from config import config

physics_expert = Agent(
    name="Mathematician",
    instructions="You are good at Physics",
)

maths_expert = Agent(
    name="Physicist",
    instructions="You are good at maths",
)

triage_agent = Agent(
    name="Triage Agent",
    instructions=(
        "You are a helpfull assistant. "
        "If users' query is math related so handoff to maths agent" 
        "If users' query is physics related so handoff to physics agent" 
    ),
    handoffs=[maths_expert, physics_expert]
)

result = Runner.run_sync(
    triage_agent,
    input="What is the sum of 10 and 30",
    run_config=config
)

print(result.final_output)
print(result.last_agent.name)