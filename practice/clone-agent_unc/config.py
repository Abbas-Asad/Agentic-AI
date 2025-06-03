import os
from dotenv import load_dotenv, find_dotenv
from agents import AsyncOpenAI, OpenAIChatCompletionsModel
from agents.run import RunConfig

# Load environment variables
load_dotenv(find_dotenv())
gemini_api_key = os.getenv("GEMINI_API_KEY")

# Setup client 
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

# Preferred model setup
model = OpenAIChatCompletionsModel(
    model="google/gemma-3n-e4b-it:free",
    openai_client=external_client
)

# Runner config
config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

