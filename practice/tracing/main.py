from agents import Agent, Runner, function_tool, handoff, RunContextWrapper, enable_verbose_stdout_logging
from config import config

# Enable verbose logging for tracing
enable_verbose_stdout_logging()

# Define a simple function tool
@function_tool
def multiply(a: int, b: int) -> int:
    """Multiply two numbers."""
    return a * b

# Define a specialized agent for handoff
specialist_agent = Agent(
    name="Specialist Agent",
    instructions="You handle advanced or specialized queries, especially about recursion or complex math.",
)

# Custom handoff handler for tracing

def on_handoff(ctx: RunContextWrapper[None]):
    print("[TRACE] Handoff event triggered!")
    return "Handoff completed by Specialist Agent."

# Register the handoff tool
handoff_tool = handoff(
    agent=specialist_agent,
    on_handoff=on_handoff,
    tool_name_override="specialist_handoff",
    tool_description_override="Use this tool to hand off advanced or specialized queries to the Specialist Agent."
)

# Main agent with both a function tool and a handoff tool
main_agent = Agent(
    name="Main Agent",
    instructions="You are a helpful assistant. Use the multiply tool for math and the specialist_handoff tool for advanced queries.",
    tools=[multiply],
    handoffs=[handoff_tool],
)

# Prompt that triggers both tool calling and handoff
prompt = (
    "What is 7 times 6? Also, I need advanced help with recursion in programming but in two lines."
)

result = Runner.run_sync(main_agent, prompt, run_config=config)
print("\nFinal Output:\n", result.final_output)

