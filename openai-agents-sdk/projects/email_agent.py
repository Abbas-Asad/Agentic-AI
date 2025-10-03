from __future__ import annotations  # For delayed type evaluation

import os
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

import chainlit as cl
from agents import Agent, Runner, AsyncOpenAI, OpenAIChatCompletionsModel, Tool
from agents.run import RunConfig
from dotenv import load_dotenv, find_dotenv

# Load environment variables from .env file
load_dotenv(find_dotenv())

# Get email credentials from environment variables.
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
if not EMAIL_ADDRESS or not EMAIL_PASSWORD:
    raise ValueError("EMAIL_ADDRESS and EMAIL_PASSWORD must be set in your .env file.")

# If you're using the Gemini API for LLM-based processing,
# ensure GEMINI_API_KEY is provided (adjust this if you use another provider).
gemini_api_key = os.getenv("GEMINI_API_KEY")
if gemini_api_key is None:
    raise ValueError("GEMINI_API_KEY environment variable not set. Please add it to your .env file.")

# Define the function that sends an email using SMTP.
def send_email(recipient: str, subject: str, body: str) -> dict:
    """
    Sends an email using SMTP.
    
    Parameters:
    - recipient (str): The recipient's email address.
    - subject (str): The subject line for the email.
    - body (str): The body text of the email.
    
    Returns:
    - dict: Contains a key "result" that summarizes the outcome.
    """
    try:
        # Create a multipart message and set headers.
        msg = MIMEMultipart()
        msg["From"] = EMAIL_ADDRESS
        msg["To"] = recipient
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))
        
        # For Gmail, use SMTP_SSL with host and port; adjust if using a different provider.
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.send_message(msg)
            
        return {"result": f"Email sent successfully to {recipient} with subject '{subject}'."}
    except Exception as e:
        return {"result": f"Failed to send email: {e}"}

# Define the Email Tool using a JSON Schema for input parameters.
email_tool = Tool(
    func=send_email,
    description="Sends an email using the provided recipient, subject, and body.",
    parameters={
        "type": "object",
        "properties": {
            "recipient": {
                "type": "string",
                "description": "The recipient's email address."
            },
            "subject": {
                "type": "string",
                "description": "The subject of the email."
            },
            "body": {
                "type": "string",
                "description": "The body text of the email."
            }
        },
        "required": ["recipient", "subject", "body"]
    },
)

# Define the instructions for the Email Automation Agent.
email_instructions = """
You are an Email Automation Assistant who helps users send automated emails.
Your tasks include:
- Extracting the recipient's email address, the subject, and the email body from the user's instruction.
- Using the provided email tool to send the email using pre-configured credentials.
- Confirming if the email has been sent successfully or reporting any encountered issues.

Use clear and concise language in your responses.
Do not reveal or log the email credentials.
"""

# Set up your LLM-based processing using the Gemini API.
external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)

model = OpenAIChatCompletionsModel(
    model="gemini-2.0-flash",
    openai_client=external_client
)

config = RunConfig(
    model=model,
    model_provider=external_client,
    tracing_disabled=True
)

# Create the Email Automation Agent with its instructions and the email tool.
email_agent: Agent = Agent(
    name="Email Automation Assistant",
    instructions=email_instructions,
    tools=[email_tool],
)

# Chainlit message handler: it will invoke the agent on incoming messages.
@cl.on_message
async def handle_message(message: cl.Message):
    result = await Runner.run(
        email_agent,
        input=message.content,
        run_config=config,
    )
    # Send the final response back to the chat.
    await cl.Message(content=result.final_output).send()
