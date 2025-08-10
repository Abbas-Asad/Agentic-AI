from agents import Agent
import inspect

def list_agent_methods(agent: Agent) -> list[str]:
    """
    Lists all non-dunder methods of an Agent instance.
    
    Args:
        agent: An instance of the Agent class
        
    Returns:
        list[str]: List of method names that don't start with '__'
    """
    # Get all methods of the agent
    all_methods = inspect.getmembers(agent, predicate=inspect.ismethod)
    
    # Filter out dunder methods (those starting with '__')
    non_dunder_methods = [method[0] for method in all_methods if not method[0].startswith('__')]
    
    return non_dunder_methods

def list_agent_properties(agent: Agent) -> list[str]:
    """
    Lists all properties of an Agent instance.
    
    Args:
        agent: An instance of the Agent class
        
    Returns:
        list[str]: List of property names that don't start with '__'
    """
    # Get all attributes of the agent
    all_attributes = inspect.getmembers(agent)
    
    # Filter out dunder attributes and methods
    properties = [
        attr[0] for attr in all_attributes 
        if not attr[0].startswith('__') 
        and not callable(getattr(agent, attr[0]))
    ]
    
    return properties

# Example usage
if __name__ == "__main__":
    # Create a sample agent
    math_agent = Agent(name="MathAssistant", instructions="You are a math expert assistant.")
    
    # Get and print all non-dunder methods
    methods = list_agent_methods(math_agent)
    print("\nNon-dunder methods of Agent class:")
    for method in methods:
        print(f"- {method}")
    
    # Get and print all properties
    properties = list_agent_properties(math_agent)
    print("\nProperties of Agent class:")
    for prop in properties:
        print(f"- {prop}") 