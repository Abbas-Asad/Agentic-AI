from agents import Agent, Runner, RunContextWrapper
from config import config
from pydantic import BaseModel
from rich import print
import nest_asyncio

from agents import output_guardrail, GuardrailFunctionOutput, OutputGuardrailTripwireTriggered
nest_asyncio.apply()

class PoliticsDiscussionOutput(BaseModel):
    is_politics_related: bool
    reason: str

guardrail_agent = Agent(
    name="Guardrail check", 
    instructions="Check if the user's question is related to politics",
    output_type=PoliticsDiscussionOutput
)

@output_guardrail
def politics_guardrail(
    ctx: RunContextWrapper[None], agent: Agent[None], output: str
) -> GuardrailFunctionOutput:       # we get the LLM response/output in 3rd parameter
    result = Runner.run_sync(guardrail_agent, input, context=ctx.context, run_config=config)
    print("\nresult.final_output:" ,result.final_output , "\n")   # just to confirm if tripwire_triggered
    
    return GuardrailFunctionOutput(
        output_info=result.final_output,
        tripwire_triggered=result.final_output.is_politics_related
    )    

agent = Agent(
    name="Assistant", 
    instructions="You are a helpful assistant. Answer queries in a line",
    output_guardrails=[politics_guardrail]
)

input = "Who is the founder of Algebra?"                                  # tripwire_triggered=False
# input = "Why do some politicians spread misinformation?"                    # tripwire_triggered=True
# input = "Why is political corruption so common in some countries?"          # tripwire_triggered=True


try:
    result = Runner.run_sync(agent, input, run_config=config)
    print(result.final_output)

except OutputGuardrailTripwireTriggered:
    print("I'm sorry, but I can't assist with political questions. If you have another question, feel free to ask!")