from agents import Agent, Runner, RunHooks, RunContextWrapper, function_tool
from config import config
from rich import print
from typing import Any
import asyncio

@function_tool
def define_kinetic_energy() -> str:
    """This tool will deliver the definition of kinetic energy."""
    return "Kinetic energy is the energy an object possesses due to its motion."

@function_tool
def define_gravity() -> str:
    """This tool will deliver the definition of gravity."""
    return "Gravity is the force that attracts two bodies toward each other."

@function_tool
def add_numbers(a: int, b: int) -> int:
    """This tool will add two numbers."""
    return a + b

@function_tool
def translate_hello() -> str:
    """This tool will translate_hello."""
    return "'Hello' in Spanish is 'Hola'."

@function_tool
def trivia_capital() -> str:
    """This will return capital of Pakistan."""
    return "The capital of Pakistan is Islamabad."

class CustomRunHooks(RunHooks):
    async def on_agent_start(self, context: RunContextWrapper[Any], agent: Agent[Any]):
        print(f"[bold green]on_agent_start[/bold green]: agent.name={agent.name}")

    async def on_agent_end(self, context: RunContextWrapper[Any], agent: Agent[Any], output: Any):
        print(f"[bold green]on_agent_end[/bold green]: agent.name={agent.name}, output={output}")

    async def on_handoff(self, context: RunContextWrapper[Any], from_agent: Agent[Any], to_agent: Agent[Any]):
        print(f"[bold yellow]on_handoff[/bold yellow]: from_agent.name={from_agent.name}, to_agent.name={to_agent.name}")

    async def on_tool_start(self, context: RunContextWrapper[Any], agent: Agent[Any], tool):
        print(f"[bold blue]on_tool_start[/bold blue]: agent.name={agent.name}, tool.name={tool.name}")

    async def on_tool_end(self, context: RunContextWrapper[Any], agent: Agent[Any], tool, result: str):
        print(f"[bold blue]on_tool_end[/bold blue]: agent.name={agent.name}, tool.name={tool.name}, result={result}")

# Agent5 (last in chain)
agent5 = Agent(
    name="Trivia Agent",
    instructions="If and only if the question is about the capital of Pakistan, use the trivia tool. Otherwise, do NOT answer, just return nothing.",
    tools=[trivia_capital],
)   
# Agent4 hands off to Agent5
agent4 = Agent(
    name="Language Agent",
    instructions="If and only if the question is to translate 'hello' to Spanish, use the tool. Otherwise, do NOT answer, just handoff to Trivia Agent.",
    tools=[translate_hello],
    handoffs=[agent5],
)
# Agent3 hands off to Agent4
agent3 = Agent(
    name="Math Agent",
    instructions="If and only if the question is to add two numbers, use the add_numbers tool. Otherwise, do NOT answer, just handoff to Language Agent.",
    tools=[add_numbers],
    handoffs=[agent4],
)
# Agent2 hands off to Agent3
agent2 = Agent(
    name="Gravity Agent",
    instructions="If and only if the question is about gravity, use the gravity tool. Otherwise, do NOT answer, just handoff to Math Agent.",
    tools=[define_gravity],
    handoffs=[agent3],
)
# Agent1 hands off to Agent2
agent1 = Agent(
    name="Physics Agent",
    instructions="If and only if the question is about kinetic energy, use the tool. Otherwise, do NOT answer, just handoff to Gravity Agent.",
    tools=[define_kinetic_energy],
    handoffs=[agent2],
)
# Top-level agent
assistant = Agent(
    name="Assistant",
    instructions="If and only if the question is about physics, handoff to Physics Agent. Otherwise, do NOT answer.",
    handoffs=[agent1],
)

# Input triggers multiple handoffs and tool calls
test_input = "What is kinetic energy? What is gravity? Add 2 and 3. Translate hello to Spanish. What is the capital of Pakistan?"

async def main():
    result = await Runner.run(
        assistant,
        test_input,
        run_config=config,
        hooks=CustomRunHooks()
    )
    print(f"[bold magenta]Final Output:[/bold magenta] {result.final_output}")

if __name__ == "__main__":
    asyncio.run(main())
