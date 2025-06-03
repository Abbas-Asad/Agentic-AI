from agents import Agent, Runner, Handoff
from config import config

# Create the main English agent
english_agent = Agent(
    name="english agent",
    instructions="You have to help in english grammar related queries. your name is abbas",
    handoffs=[],  # Empty list for now, you can add handoffs later
    
)

# Create a grammar specialist agent
grammar_agent = Agent(
    name="grammar specialist",
    instructions="You are a grammar specialist. You help with complex grammar rules and sentence structure. Your name is grammar_expert"
)

# Create a vocabulary agent
vocabulary_agent = Agent(
    name="vocabulary expert",
    instructions="You are a vocabulary expert. You help with word meanings, synonyms, and antonyms. Your name is vocab_master"
)

# Create handoffs for different types of queries
grammar_handoff = Handoff(
    name="grammar_handoff",
    instructions="Hand off to grammar specialist for complex grammar queries",
    target_agent=grammar_agent
)

vocabulary_handoff = Handoff(
    name="vocabulary_handoff",
    instructions="Hand off to vocabulary expert for word-related queries",
    target_agent=vocabulary_agent
)

# Update the main agent with handoffs
english_agent = Agent(
    name="english agent",
    instructions="You have to help in english grammar related queries. your name is abbas",
    handoffs=[grammar_handoff, vocabulary_handoff]
)

# Clone the agent with modified instructions
agent = english_agent.clone(
    instructions="You have to help in english grammar related queries. your name is asad"
)

result = Runner.run_sync(agent, "what are your expertise? tell me in one line and also tell your name", run_config=config)
# print(result.final_output)
# print(dir(agent))
print(agent)