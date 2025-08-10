from typing import Any

from pydantic import BaseModel

from agents import RunContextWrapper, FunctionTool, Agent, Runner, enable_verbose_stdout_logging
from config import config

enable_verbose_stdout_logging()

def do_some_work(data: str) -> str:
    # return "done"
    raise ValueError("Not found")


class FunctionArgs(BaseModel):
    username: str
    age: int


async def run_function(ctx: RunContextWrapper[Any], args: str) -> str:
    parsed = FunctionArgs.model_validate_json(args)
    try:
        return do_some_work(data=f"{parsed.username} is {parsed.age} years old")
    except Exception as err:
        return f"Abbas don't want to show you this data"

tool_1 = FunctionTool(
    name="process_user",
    description="Processes extracted user data",
    params_json_schema=FunctionArgs.model_json_schema(),
    on_invoke_tool=run_function,
)

agent = Agent(name="Assistant", instructions="You are a helpful assistant.", tools=[tool_1])

input='{"username": "John", "age": 30}, process this data'
result = Runner.run_sync(agent, input, run_config=config)
print(result.final_output)
# print(tool_1)