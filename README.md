
<!-- Welcome to my **personal learning vault** for everything related to **Agentic AI**.  
This repository is where I document my journey, experiments, resources, and notes — a mix of **code vlogging**, tutorials, and practice projects.  
If you're also exploring Agentic AI, this repo can serve as a structured reference. -->

<!-- ---

## 📖 About This Repository
This is not just a collection of random code — it’s my step-by-step learning path in **Agentic AI**, covering:
- **Fundamentals** of Generative AI and LLMs
- **Prompt Engineering** best practices
- **OpenAI Agents SDK** concepts and tools
- **Multi-Agent Systems**
- **Integrations** with APIs and frameworks
- **My custom tools & utilities**

---

## 🗂 Folder Structure & Topics

```
Agentic-AI-with-Abbas/
│
├── 01-generative-ai-basics/       # Core AI & LLM concepts
├── 02-prompt-engineering/         # Prompt design techniques
├── 03-openai-agents-sdk/          # Agents SDK learning & tools
├── 04-multi-agent-systems/        # Multi-agent orchestration
├── 05-memory-and-context/         # Agent memory systems
├── 06-agent-tools-library/        # My custom AI tools
├── 07-ai-integrations/            # APIs, LangChain, HuggingFace
├── 08-markdown-tips/              # Markdown cheatsheets & tips
├── 09-useful-resources/           # Links, videos, blogs
└── README.md                      # This file
```

--- -->



<!-- ## OpenAI Agents SDK Boilerplate

```python
from agents import Agent, Runner
from agentsdk_gemini_adapter import config

# Create an agent using Agent class 
agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant.",
)

# Pass the Gemini configuration in run_config to any Runner method
result = Runner.run_sync(agent, "What is 2 + 2?", run_config=config)

print("Result:", result.final_output)
```

### Prerequisites for this boilerplate

- Make sure that GEMINI_API_KEY is set
- [OpenAI Agents SDK](https://openai.github.io/openai-agents-python/) is already installed -->

## Useful Resources

### Python
[Understanding Python Dataclasses](https://www.geeksforgeeks.org/python/understanding-python-dataclasses/)  
[Pydantic Cheatsheet](https://michaelcurrin.github.io/dev-cheatsheets/cheatsheets/python/libraries/pydantic.html)  
[Python Type hints Cheatsheet](https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html)  

### Agentic AI
[LLM Internal Working in 1 video](https://youtu.be/wjZofJX0v4M?si=jPhFRK67iVzj3RBD)  
[AI Agents Explained in easy words by NVIDIA](https://www.nvidia.com/en-us/glossary/ai-agents/)  
[AI Agents All Definitions](https://app.mindstudio.ai/share/public/asset/46DOHFvzkfNowf3B6nT9LS)  
[OpenAI Agents SDK Gemini Adapter](https://pypi.org/project/agentsdk-gemini-adapter/)  
[OpenAI Agents SDK Tutorial](https://www.datacamp.com/tutorial/openai-agents-sdk-tutorial)  
[AI Agents Startup Ideas in detail](https://github.com/panaversity/learn-agentic-ai/tree/main/-01_lets_get_started/03_from_llms_to_stateful_long_runningl_multi_agents)  
<!-- [AI Agents Cheatsheet](https://media.datacamp.com/cms/ai-agents-cheat-sheet.pdf)   -->

### Custom GPTs for OpenAI SDK
[Custom GPT #1](https://chatgpt.com/g/g-67ecc41ba33081919fe5428c87e78373-agents-sdk)  
[Custom GPT #2](https://chatgpt.com/g/g-67d2c11e296c8191b18035f6319982e3-python-ai-agent-helper)  


### n8n (Workflow Automation)
  
[n8n Official Documentation](https://docs.n8n.io/)  
[n8n GitHub Repository](https://github.com/n8n-io/n8n)  
[n8n Workflows Marketplace](https://n8n.io/workflows)  
[n8n Oficial Playlist](https://www.youtube.com/playlist?list=PLlET0GsrLUL5HKJk1rb7t32sAs_iAlpZe)  

<!-- [Awesome n8n (Community Resources)](https://github.com/ahmadbilaldev/awesome-n8n)   -->
<!-- [How to Build AI Agents with n8n](https://n8n.io/blog/ai-agents-with-n8n)   -->


### Prompt Engineering
[Prompt Engineering Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)  
[Free LLM Playgrounds to test Model Parameters](https://llm-explorer.com/static/blog/?id=free-llm-playgrounds)

### Tech Stack
[AI Agents Tech Stack](https://www.linkedin.com/posts/rakeshgohel01_ai-agents-are-about-90-software-engineering-activity-7353405600610881536-D36M?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE4LvzIBUre-SsOdMUHO2iov_O9bjpaz5eE) 

### Cheatsheet
[LLM Usage Cheatsheet](https://github.com/Abbas-Asad/Agentic-AI/blob/main/cheatsheets/llm_usage_cheatsheet.gif)  
[AI Agents Cheatsheet](https://media.datacamp.com/cms/ai-agents-cheat-sheet.pdf)  
[MCP Cheatsheet](https://github.com/Abbas-Asad/Agentic-AI/blob/main/cheatsheets/mcp_cheatsheet.gif)  


### Add-ons 

<!-- [AI Agents Ecosystem](https://www.linkedin.com/posts/rakeshgohel01_ai-agents-are-about-90-software-engineering-activity-7353405600610881536-D36M?utm_source=share&utm_medium=member_desktop&rcm=ACoAAE4LvzIBUre-SsOdMUHO2iov_O9bjpaz5eE)   -->
<!-- [Prompt Engineering Guide](https://github.com/dair-ai/Prompt-Engineering-Guide)   -->
[Biggest Collection of ready made agents on Internet](https://github.com/Shubhamsaboo/awesome-llm-apps)  
[Build Effective AI Agents](https://www.anthropic.com/engineering/building-effective-agents) 
 

[Top 7 Typescript Frameworks for AI Agents](https://medium.com/@wahyuikbal/top-7-typescript-frameworks-for-ai-agents-08710bc7d5ff)  
[The 12 Best AI Coding Assistants in 2025](https://www.datacamp.com/blog/best-ai-coding-assistants)  
[The Best AI Agents in 2025: Tools, Frameworks, and Platforms Compared](https://www.datacamp.com/blog/best-ai-agents)  

---

### About Me
I’m **[Abbas](https://www.linkedin.com/in/agentic-ai-developer/)**, a developer, contributor, student and at the same time a teacher.  



<!-- 

## 🔗 Useful Resources

### Official Docs
- [OpenAI Agents SDK Documentation](https://api.openai.com/docs/agents)
- [LangChain Docs](https://python.langchain.com/docs/)
- [HuggingFace](https://huggingface.co/docs)

### Recommended Videos
- [OpenAI Agents SDK Walkthrough – YouTube](#)
- [Prompt Engineering Crash Course – YouTube](#)

### Blogs & Articles
- [Understanding Multi-Agent Systems](#)
- [Best Practices in Agent Tool Design](#)

---

## 🛠 Tech Stack & Tools
- **Languages:** Python, TypeScript
- **AI SDKs:** OpenAI Agents SDK, LangChain
- **Utilities:** Markdown, GitHub Projects
- **Other Tools:** HuggingFace, REST APIs

--- -->
