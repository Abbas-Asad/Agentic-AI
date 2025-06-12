from config import config
from agents import Agent, Runner, handoff, RunContextWrapper, Handoff,enable_verbose_stdout_logging
from agents.extensions import handoff_filters
from pydantic import BaseModel

enable_verbose_stdout_logging()
# Create a custom handoff with description override

class EscalationData(BaseModel):
    reason: str

# def handle_handoff(ctx: RunContextWrapper[None]):
#     print(f"Handoff is called 🥹")
def handle_handoff(ctx: RunContextWrapper[None], input_data: EscalationData):
    print(f"Handoff is called 🥹  and Billing agent called with reason: {input_data.reason}")
    print(f"handoff is called 🥹 and the input is query: {input_data.query} amount: {input_data.amount}")
    print(f"query_type: {type(input_data.query)} amount_type: {type(input_data.amount)}")

billing_agent = Agent(
    name="Billing Agent",
    instructions="You will handle billing related queries.",
)

# billing_handoff = handoff(
#     agent=billing_agent,
#     tool_name_override="custom_billing_agent",
#     tool_description_override="This handoff is specifically for handling billing and payment related queries",
#     on_handoff=handle_handoff,
#     input_type=EscalationData,
#     input_filter=handoff_filters.remove_all_tools
# )

triage_agent = Agent(
    name="Triage Agent",
    instructions="You are a helpful assistant. Call the billing_handoff tool if needed",
    handoffs=[billing_agent],
)
# input = "I need to dispute a charge on my last invoice and get a refund my amount was $99 an the currency charge is in dollars"
input = "I need to dispute a charge on my last invoice and get a refund"
# input = "What is conjunction in english"
result = Runner.run_sync(triage_agent, input, run_config=config)
print(result.final_output)
# print(billing_handoff.__class__)

# print(billing_handoff)