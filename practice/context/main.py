# import asyncio
from dataclasses import dataclass
from config import config

from agents import Agent, RunContextWrapper, Runner, function_tool, enable_verbose_stdout_logging

@dataclass
class UserInfo:  
    name: str
    uid: int
    age: str

@function_tool
def fetch_user_age(wrapper: RunContextWrapper[UserInfo]) -> str:  
    # """Returns the age of the user"""
    return f"User {wrapper.context.name} is {wrapper.context.age} years old"

def main():
    user_info = UserInfo(name="Abbas", uid=123, age=22)

    enable_verbose_stdout_logging()  # Enable logging before agent execution

    agent = Agent[UserInfo](  
        name="Assistant",
        instructions="You are a helpful assistant.",
        tools=[fetch_user_age],
    )

    result = Runner.run_sync(  
        starting_agent=agent,
        input="What is the name of the user?",
        context=user_info,
        run_config=config
    )

    print(result.final_output)  
    # The user John is 47 years old.

# if __name__ == "__main__":
#     asyncio.run(main())
main()