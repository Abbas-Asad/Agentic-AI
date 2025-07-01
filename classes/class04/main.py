from agents import OpenAIChatCompletionsModel, Agent, Runner, RunConfig, AsyncOpenAI
import os

API_KEY= os.getenv("GEMINI_API_KEY")

client = AsyncOpenAI(
    api_key=API_KEY,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai"
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=client
)

config=RunConfig(
    model=model
)

agent=Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    model=model
)

result=Runner.run_sync(
    starting_agent=agent,
    input="What is the capital of Pakistan?",
    run_config=config
)

print(result.final_output)