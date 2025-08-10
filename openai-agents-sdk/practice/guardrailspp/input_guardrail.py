from agents import Agent, Runner, RunContextWrapper
from config import config
from pydantic import BaseModel
from rich import print
import nest_asyncio

from agents import input_guardrail, GuardrailFunctionOutput, InputGuardrailTripwireTriggered, TResponseInputItem
nest_asyncio.apply()

class ExceptMathQueriesOutput(BaseModel):
    is_query_except_math: bool
    reason: str
    answer: str

guardrail_agent = Agent(
    name="Guardrail check", 
    instructions="Check if the user is asking anything except math.",
    output_type=ExceptMathQueriesOutput,
)

@input_guardrail
def except_math_guardrail(
    ctx: RunContextWrapper[None], agent: Agent[None], input: str | list[TResponseInputItem]
) -> GuardrailFunctionOutput:       # we get the USER input/query in 3rd parameter
    result = Runner.run_sync(guardrail_agent, input, context=ctx.context, run_config=config)
    print("\nresult.final_output:" ,result.final_output , "\n")   # just to confirm if tripwire_triggered

    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_query_except_math,
    )


math_agent = Agent(
    name="Math agent", 
    instructions="You are a math expert assistant. Answer queries in a line",
    input_guardrails=[except_math_guardrail]
)

input = "What is the diff bw denominator and numerator?"          # maths question # False
# input = "What is the diff bw verb and adverb?"                    # english question # True
# input = "What is the diff bw eletron and neutron?"                # science question # True

try:
    result = Runner.run_sync(math_agent, input, run_config=config)
    print(result.final_output)

except InputGuardrailTripwireTriggered:
    print("I'm sorry, but I can only assist with mathematics related questions. If you math related question, feel free to ask!")