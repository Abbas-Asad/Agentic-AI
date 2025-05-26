import chainlit as cl
from agents import Agent, Runner
from config import config

recipe_generator_instructions = """
You are ChefGPT, an expert culinary assistant. Provide recipes in this EXACT structure:

[Recipe Name] 
Cuisine: [Type] | Prep: [Time] | Cook: [Time] | Serves: [X] persons

**Ingredients**:
  In exact order of use:
- [Quantity] [Ingredient] ([Preparation if needed])  
  Example: "1.5 cups basmati rice (soaked 30 mins)"
- [Quantity] [Protein]  
  Example: "500g chicken thighs (bone-in)"
- [Quantity] [Spices/Seasonings] 
  Example: "2 tsp garam masala"

**Steps**:
1. [Action + Timing]  
   Example: "Heat ghee in pan (2 mins medium heat)"
2. [Main cooking process]
3. [Layering/Combining]
4. [Critical timing step]
5. [Final serving instruction]

**Pro Tips**:
- [Special technique] 
- [Substitution] 
- [Storage tip]

Keep responses under 300 words. Never use sub-headers in ingredients. List EVERYTHING under main Ingredients section.
"""

# 🎯 Create Product Detail Assistant Agent
recipe_agent: Agent = Agent(
    name="Product Detail Assistant",
    instructions=recipe_generator_instructions,
)


# First Message When Chat Starts
@cl.on_chat_start
async def handle_chat_start():
    cl.user_session.set("history", [])
    await cl.Message(
        content=(
            "**Hello! I’m ChefGPT, your personal recipe generator.**\n\n"
            "Tell me what you’d like to cook today:\n"
            "- A specific dish name (e.g., “Chicken Tikka Masala”)\n"
            "- A set of ingredients you have on hand\n"
            "- A cuisine or dietary style (e.g., “vegetarian Italian”)\n\n"
            "I’ll give you a full ingredient list, step‑by‑step instructions, and useful tips. Let’s get cooking! 👩‍🍳"
        )
    ).send()


@cl.on_message
async def handle_message(message: cl.Message):
    history = cl.user_session.get("history")

    history.append({"role": "user", "content": message.content})
    
    result = await Runner.run(
        recipe_agent,
        input=history,
        run_config=config,
    )

    history.append({"role": "assistant", "content": result.final_output})
    cl.user_session.set("history", history)
    await cl.Message(content=result.final_output).send()