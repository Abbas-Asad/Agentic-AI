import asyncio
from config import config
from dataclasses import dataclass
from agents import Agent, Runner, RunContextWrapper, enable_verbose_stdout_logging

enable_verbose_stdout_logging()

async def main():
    @dataclass
    class UserInfo:
        name: str
        interest: str
        food: str

    user1 = UserInfo(name="Abbas", interest="Agentic AI", food="Chicken Fajita Pizza")
    user2 = UserInfo(name="Fasih", interest="Python Programming", food="Zinger Burger")

    def dynamic_instructions(wrapper: RunContextWrapper[UserInfo], agent: Agent[UserInfo]):
        """This is the context of user"""
        return f"The user name is: {wrapper.context.name}. He is interested in: {wrapper.context.interest}. His favourite food is {wrapper.context.food} so you have to make him feel comfortable like you're his assistant"


    agent = Agent[UserInfo](name="assistant", instructions=dynamic_instructions)

    result = await Runner.run(
        agent,
        input="Hello!",
        run_config=config,
        # context=user1,
        context=user2,
    )

    print(agent.instructions)
    print(result.final_output)

asyncio.run(main())