from agents import Agent, Runner, enable_verbose_stdout_logging
from agentsdk_gemini_adapter import config

enable_verbose_stdout_logging()

agent = Agent(
    name="", 
    instructions="You are a helpful assistant"
    )

result = Runner.run_sync(
    agent, 
    "Write a line about Pakistan.",
    run_config=config
    )

print(result.final_output)