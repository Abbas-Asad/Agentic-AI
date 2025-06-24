from config import config
from dataclasses import dataclass
from custom_tools import get_all_subjects, get_school_days, get_all_parts_of_speech
from agents import Agent, Runner, RunContextWrapper

@dataclass
class Student:
    name: str
    sid: int

student1 = Student(name="Abbas", sid=25364)

def dynamic_instructions(
        context: RunContextWrapper[Student],
        agent: Agent[Student]
) -> str:
    return f"Studentname is {context.context.name}. You have to solve his queries. Also tell the user that you also have tools like {agent.get_all_tools} so that he can assign you task accordingly."

agent = Agent[Student](
    name= "Assistant",
    instructions= dynamic_instructions,
    tools=[get_all_subjects, get_school_days, get_all_parts_of_speech]
)

result = Runner.run_sync(
    agent,
    input="Hello",
    run_config=config,
    context=student1
)

print(result.final_output)


# instructions type =   Callable[[RunContextWrapper[TContext], Agent[TContext]],MaybeAwaitable[str],]
# docs =                """The instructions for the agent. Will be used as the "system prompt" when this 
# agent is invoked. Describes what the agent should do, and how it responds.

# Can either be a string, or a function that dynamically generates instructions for the agent. If
# you provide a function, it will be called with the context and the agent instance. It must
# return a string.
# """

# =============My Notes=============
# So you can create dynamic instructions via function that's why is it's callable.
# When you provide a function, it will be called with the context and the agent instance. so that it can get dynamic properties of context like user name & agent like tools.