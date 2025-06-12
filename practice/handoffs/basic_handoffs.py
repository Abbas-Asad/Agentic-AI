from config import config
from agents import Agent, Runner, handoff, enable_verbose_stdout_logging
# from pydantic import BaseModel

english_agent = Agent(
    name="English Agent",
    instructions="You handle all english language related queries.",
    handoff_description="This can be used in english language related queries"

)

custom_handoffs = handoff(
    agent=english_agent,
    tool_name_override="english_tool",
    tool_description_override="You are an english language tool",
)

triage_agent = Agent(
    name="Triage Agent",
    instructions="You will handle user queries.",
    handoffs=[custom_handoffs],
)

enable_verbose_stdout_logging()

result = Runner.run_sync(triage_agent, "What is english? answer me in just 10 words. You can use your tools", run_config=config)
print(result.final_output)