from agents import Agent, handoff, RunContextWrapper, Runner, enable_verbose_stdout_logging
from config import config

# enable_verbose_stdout_logging()

def on_handoff(ctx: RunContextWrapper[None]):
    print("Handoff called")
    return "Handoff was successful!"

# Create a target agent that will handle the handoff
target_agent = Agent(
    name="Target Agent",
    instructions="You are a specialized agent that handles specific tasks."
)

# Create the main agent
agent = Agent(
    name="Main Agent",
    instructions="You are a helpful assistant. Use the custom_handoff_tool when you need to hand off to a specialized agent."
)

handoff_obj = handoff(
    agent=target_agent,  # This is the agent that will handle the handoff
    on_handoff=on_handoff,
    tool_name_override="custom_handoff_tool",
    tool_description_override="Use this tool when you need to hand off to a specialized agent for specific tasks"
)

# Register the handoff with the main agent
agent.handoffs = [handoff_obj]

result = Runner.run_sync(
    agent,
    "I need specialized help with a complex task that requires a handoff",
    run_config=config
)
print(result.final_output)