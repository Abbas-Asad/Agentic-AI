from PyPDF2 import PdfReader
import chainlit as cl
from agents import Agent, Runner, function_tool
from typing import Dict, Any
from config import config

# ========== 🛠️ Tools ==========
@function_tool
def extract_text_from_pdf(file_path: str) -> Dict[str, Any]:
    """Extract text from a PDF file."""
    try:
        with open(file_path, "rb") as f:
            reader = PdfReader(f)
            text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
        return {"text": text}
    except Exception as e:
        return {"error": f"Error reading PDF: {str(e)}"}


@function_tool
def analyze_resume_text(resume_text: str) -> Dict[str, Any]:
    """Analyze resume text and give suggestions."""
    return {
        "analysis": f"""
✅ **Resume Analysis**:

**Extracted Summary**:  
{text_summary(resume_text)}

**Suggestions**:
- Add more quantifiable achievements.
- Ensure contact info is visible.
- Highlight technical and soft skills.
        """.strip()
    }

def text_summary(text: str) -> str:
    return text[:500] + ("..." if len(text) > 500 else "")

# ========== 🧠 Agent ==========
resume_agent = Agent(
    name="Resume Analyzer",
    instructions="""
You are a professional Resume Analyzer.

When a resume is uploaded or pasted, extract the key info:
- Name, Email, Phone, Skills, Experience, Education
Then, give clear suggestions for improvement.
""",
    tools=[extract_text_from_pdf, analyze_resume_text]
)

# ========== 💬 Chainlit Logic ==========
@cl.on_chat_start
async def start():
    await cl.Message(content="Hi! Upload your resume (PDF) or paste it as text. I’ll analyze it.").send()


@cl.on_message
async def on_message(message: cl.Message):
    if message.elements:
        for element in message.elements:
            if element.name.endswith(".pdf"):
                pdf_path = element.path
                result = extract_text_from_pdf(pdf_path)

                if "text" in result:
                    analysis = await Runner.run(
                        resume_agent,
                        input=result["text"],
                        run_config=config
                    )
                    await cl.Message(content=analysis.final_output).send()
                else:
                    await cl.Message(content=result["error"]).send()
                return
    else:
        analysis = await Runner.run(
            resume_agent,
            input=message.content,
            run_config=config
        )
        await cl.Message(content=analysis.final_output).send()
