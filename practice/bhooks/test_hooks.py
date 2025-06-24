from agents import Agent, Runner, AgentHooks, RunContextWrapper, enable_verbose_stdout_logging, function_tool
from config import config
from rich import print
from typing import Any
import asyncio

# enable_verbose_stdout_logging()

@function_tool
def define_kinetic_energy() -> str:
    """This tool will deliver the definition of kinetic energy."""
    return "Kinetic energy is the energy an object possesses due to its motion."

class CustomAgentHooks(AgentHooks):
    async def on_start(self, context: RunContextWrapper[Any], agent: Agent[Any]):
        print(f"[bold green]on_start[/bold green]: Agent '{agent.name}' is starting")

    async def on_end(self, context: RunContextWrapper[Any], agent: Agent[Any], output: Any):
        print(f"[bold green]on_end[/bold green]: Agent '{agent.name}' is ending. Output: {output}")

    async def on_handoff(self, context: RunContextWrapper[Any], agent: Agent[Any], source: Agent[Any]):
        print(f"[bold yellow]on_handoff[/bold yellow]: Agent '{agent.name}' received handoff from '{source.name}'")

    async def on_tool_start(self, context: RunContextWrapper[Any], agent: Agent[Any], tool):
        print(f"[bold blue]on_tool_start[/bold blue]: Agent '{agent.name}' is starting tool '{tool.name}'")

    async def on_tool_end(self, context: RunContextWrapper[Any], agent: Agent[Any], tool, result: str):
        print(f"[bold blue]on_tool_end[/bold blue]: Agent '{agent.name}' finished tool '{tool.name}' with result: {result}")

physics_agent = Agent(
    name="Physics Agent",
    instructions="You are a physics expert agent. Always use the tool to answer",
    tools=[define_kinetic_energy],
    hooks=CustomAgentHooks()
)

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant. Use the add_numbers tool if asked to add numbers. You can handoff to physics_agent if needed.",
    handoffs=[physics_agent],
    hooks=CustomAgentHooks()
)

# input = "Add 2 and 3 using the tool."
input = "What is kinetic energy? answer in 1 line"

async def main():
    result = await Runner.run(
        agent,
        input,
        run_config=config,
    )
    print(f"[bold magenta]Final Output:[/bold magenta] {result.final_output}")

if __name__ == "__main__":
    asyncio.run(main())
