from dataclasses import dataclass
from typing import Generic, TypeVar, Callable,       List, Optional, Union, ClassVar

TContext = TypeVar("TContext")

@dataclass
class RunContextWrapper(Generic[TContext]):
  """This wraps the context object that you passed"""

  context: TContext
  """The context object (or None), passed by you"""
# var: list[str] = ["a", "b", "c"]
var: Optional[str] = "abbas" 
@dataclass
class Agent(Generic[TContext]):
#   name: str
#   instructions: str | Callable[[RunContextWrapper[TContext], "Agent[TContext]"], str] | None = None
    name: str
    """The name of the agent."""

    instructions: (
        str
        | 
        Callable[
            [RunContextWrapper[TContext], 'Agent[TContext]'],
            str,
        ]
        | None
    ) = None

@dataclass
class GovernerHouseStudent:
  name: str
  age: int
  student_id: int

student_1 = GovernerHouseStudent(name="Abbas", age=22, student_id=238960)

def fetch_student_name(
    context: RunContextWrapper[GovernerHouseStudent],
    agent: Agent[GovernerHouseStudent]
):
  return f"Student name is: {student_1.name}"

agent = Agent[GovernerHouseStudent](name="Assistant", instructions=fetch_student_name)

# Create a context wrapper with the student
context = RunContextWrapper(context=student_1)

# Print the agent's name
print(f"Agent name: {agent.name}")

# Execute the agent's instructions if it's a callable
if callable(agent.instructions):
    result = agent.instructions(context, agent)
    print(f"Agent response: {result}")
else:
    print(f"Agent instructions: {agent.instructions}")

# Print student details
print(f"\nStudent Details:")
print(f"Name: {student_1.name}")
print(f"Age: {student_1.age}")
print(f"Student ID: {student_1.student_id}")
 