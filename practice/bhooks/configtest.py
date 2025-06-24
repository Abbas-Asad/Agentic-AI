import os
from dotenv import find_dotenv, load_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel, RunConfig

load_dotenv(find_dotenv())
a= os.getenv()

ex_c=AsyncOpenAI(
    api_key=a,
    base_url=""
)

m=OpenAIChatCompletionsModel(
    model="",
    openai_client=ex_c
)

RunConfig(
    model=m,
    model_provider=ex_c,
    tracing_disabled=True
)