# Complex Scenario: You have a parent agent with both RunHooks and AgentHooks configured. This parent agent uses an agent-as-tool (created via agent.as_tool()) that also has its own AgentHooks. The child agent-as-tool calls another regular function tool during its execution.
# Question: What is the correct sequence of hook executions when the parent agent invokes the agent-as-tool?

from agents import Agent, Runner, RunHooks, AgentHooks, RunContextWrapper, Tool, function_tool
from config import config
from typing import Any
from rich import print

# Simple function tool
@function_tool
def add_numbers(a: int, b: int) -> str:
    result = a + b
    return f"The sum of {a} and {b} is {result}."

# Parent RunHooks - Run level hooks
class ParentRunHooks(RunHooks):
    async def on_agent_start(self, context: RunContextWrapper[Any], agent: Agent[Any]):
        print("[bold magenta]Parent(Runhook): Agent is Started[/bold magenta]")

    async def on_agent_end(self, context: RunContextWrapper[Any], agent: Agent[Any], output: Any):
        print("[bold magenta]Parent(Runhook): Agent is Ended[/bold magenta]")

    async def on_tool_start(self, context: RunContextWrapper[Any], agent: Agent[Any], tool: Tool):
        print("[bold magenta]Parent(Runhook): Agent tool is Started[/bold magenta]")

    async def on_tool_end(self, context: RunContextWrapper[Any], agent: Agent[Any], tool: Tool, result: str):
        print("[bold magenta]Parent(Runhook): Agent tool is Ended[/bold magenta]")

# Parent AgentHooks - Agent level hooks
class ParentAgentHooks(AgentHooks):
    async def on_start(self, context: RunContextWrapper[Any], agent: Agent[Any]):
        print("[bold green]Parent(Agenthook): Agent is Started[/bold green]")

    async def on_end(self, context: RunContextWrapper[Any], agent: Agent[Any], output: Any):
        print("[bold green]Parent(Agenthook): Agent is Ended[/bold green]")

    async def on_tool_start(self, context: RunContextWrapper[Any], agent: Agent[Any], tool: Tool):
        print("[bold green]Parent(Agenthook): Agent tool is Started[/bold green]")

    async def on_tool_end(self, context: RunContextWrapper[Any], agent: Agent[Any], tool: Tool, result: str):
        print("[bold green]Parent(Agenthook): Agent tool is Ended[/bold green]")

# Child AgentHooks - Agent level hooks for child agent
class ChildAgentHooks(AgentHooks):
    async def on_start(self, context: RunContextWrapper[Any], agent: Agent[Any]):
        print("[bold yellow]Child(Agenthook): Agent is Started[/bold yellow]")

    async def on_end(self, context: RunContextWrapper[Any], agent: Agent[Any], output: Any):
        print("[bold yellow]Child(Agenthook): Agent is Ended[/bold yellow]")

    async def on_tool_start(self, context: RunContextWrapper[Any], agent: Agent[Any], tool: Tool):
        print("[bold yellow]Child(Agenthook): Agent tool is Started[/bold yellow]")

    async def on_tool_end(self, context: RunContextWrapper[Any], agent: Agent[Any], tool: Tool, result: str):
        print("[bold yellow]Child(Agenthook): Agent tool is Ended[/bold yellow]")

# Create child agent (will become agent-as-tool)
child_agent = Agent(
    name="Child Agent",
    instructions="You are a child agent that can add numbers. Use the add_numbers tool when asked to add numbers.",
    tools=[add_numbers],
    hooks=ChildAgentHooks()
)

# Create parent agent with both RunHooks and AgentHooks
parent_agent = Agent(
    name="Parent Agent",
    instructions="You are a parent agent. When asked to add numbers, use the child agent tool.",
    tools=[child_agent.as_tool(
        tool_name="child_agent_tool",
        tool_description="A tool that can add numbers"
    )],
    hooks=ParentAgentHooks()
)

def main():
    print("\nSequence of Hooks Execution:")
    
    result = Runner.run_sync(
        parent_agent,
        "Add 20 and 40",
        run_config=config,
        hooks=ParentRunHooks()
    )
    
    print(f"\n{result.final_output}")

main()