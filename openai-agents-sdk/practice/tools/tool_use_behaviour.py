from agents import Agent, Runner, function_tool, RunContextWrapper, ToolsToFinalOutputResult, enable_verbose_stdout_logging, FunctionToolResult
from config import config

enable_verbose_stdout_logging()

@function_tool
def check_product_price(product: str) -> float:
    """A tool that checks the price of different products in our store.
    
    Args:
        product (str): The name of the product. Currently supports:
            - "laptop"
            - "smartphone"
            - "headphones"
            - "tablet"
    
    Returns:
        float: The price of the product in dollars
    """
    prices = {
        "laptop": 999.99,
        "smartphone": 699.99,
        "headphones": 199.99,
        "tablet": 499.99
    }
    return prices.get(product, 0.0)

@function_tool
def calculate_discount(price: float, discount_percent: float) -> float:
    """A tool that calculates the discounted price.
    
    Args:
        price (float): Original price of the product
        discount_percent (float): Discount percentage (0-100)
    
    Returns:
        float: The final price after discount
    """
    if not 0 <= discount_percent <= 100:
        return price
    
    discount = price * (discount_percent / 100)
    return price - discount

def shopping_assistant_behavior(context: RunContextWrapper[None], tool_results: list[FunctionToolResult]) -> ToolsToFinalOutputResult:
    """Smart shopping assistant behavior that helps users with product prices and discounts.
    
    Rules:
    1. If price is too high (>$800), suggest a discount
    2. If price is reasonable, show it directly
    3. For discount calculations, show the savings amount
    
    Args:
        context: The run context
        tool_results: List of tool results
    
    Returns:
        ToolsToFinalOutputResult: Contains result and whether to stop or continue
    """
    if not tool_results:
        return ToolsToFinalOutputResult(final_output="", is_final_output=False)
    
    tool = tool_results[0]
    tool_name = tool.tool.name
    output = tool.output

    # For price checks
    if tool_name == "check_product_price":
        price = float(output)
        if price > 800:
            return ToolsToFinalOutputResult(
                final_output=f"Price: ${price:.2f} (This is a premium product! Would you like to know about available discounts?)",
                is_final_output=True
            )
        else:
            return ToolsToFinalOutputResult(
                final_output=f"Price: ${price:.2f}",
                is_final_output=True
            )
    
    # For discount calculations
    if tool_name == "calculate_discount":
        original_price = float(tool.tool.args.get("price", 0))
        discounted_price = float(output)
        savings = original_price - discounted_price
        
        return ToolsToFinalOutputResult(
            final_output=f"Original Price: ${original_price:.2f}\nDiscounted Price: ${discounted_price:.2f}\nYou Save: ${savings:.2f}",
            is_final_output=True
        )
    
    # For other cases
    return ToolsToFinalOutputResult(
        final_output=str(output),
        is_final_output=False
    )

# 🤖 Smart Shopping Assistant Setup
agent = Agent(
    name="SmartShoppingAssistant",
    instructions="You are a helpful shopping assistant. Help users check product prices and calculate discounts.",
    tools=[check_product_price, calculate_discount],
    tool_use_behavior=shopping_assistant_behavior
)

# 🧪 Test Inputs
test_inputs = [
    "What's the price of a laptop?",                     # Will show price and suggest discount
    "How much does a tablet cost?",                      # Will show price directly
    "What's the price of a smartphone with 20% discount?",  # Will show original and discounted price
    "Tell me the price of headphones",                   # Will show price directly
]

print("🛍️ Welcome to Smart Shopping Assistant! 🛍️")
print("==========================================")

for input_text in test_inputs:
    print(f"\n🧾 Customer: {input_text}")
    result = Runner.run_sync(agent, input_text, run_config=config)
    print(f"🤖 Assistant: {result.final_output}")
    print("------------------------------------------")
