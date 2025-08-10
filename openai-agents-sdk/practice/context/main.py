import asyncio
from config import config
from dataclasses import dataclass
from agents import Agent, Runner, RunContextWrapper, function_tool

@dataclass
class UserInfo:
    name: str
    age: int
    userid: int
    password: str

@function_tool
def fetch_user_info(wrapper: RunContextWrapper[UserInfo]):
    """This will fetch user name, age, userid and password"""
    return f"Name: {wrapper.context.name}| Age: {wrapper.context.age}"

async def main(): 
    user1 = UserInfo(name="Abbas", age=22, userid=123, password="i#luy5^6_5u56nu")

    agent = Agent[UserInfo](name="assistant", tools=[fetch_user_info])
    # Instructions are not needed here

    result = await Runner.run(
        agent,
        input="What is the name, age and userid of user",
        run_config=config,
        context=user1
    )

    print("=====Local Context=====")
    print(result.final_output)
    # The name is Abbas, the age is 22. I don't have the userid or I don't have access to the userid

if __name__ == "__main__":
    asyncio.run(main())