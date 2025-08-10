from config import config
from agents import Agent, Runner, function_tool, enable_verbose_stdout_logging
# from agents.agent import StopAtTools

enable_verbose_stdout_logging()

@function_tool
def calculator(operation: str, a: float, b: float) -> float:
    """A calculator tool that performs basic arithmetic operations between two numbers.
    
    This tool can perform four basic arithmetic operations: addition, subtraction, multiplication, and division.
    It takes two numbers and an operation type as input and returns the result of the calculation.
    
    Args:
        operation (str): The arithmetic operation to perform. Must be one of: "add", "subtract", "multiply", "divide"
        a (float): The first number in the calculation
        b (float): The second number in the calculation
    
    Returns:
        float: The result of the arithmetic operation. Returns an error message if:
            - The operation is invalid
            - Division by zero is attempted
    
    Example:
        calculator("add", 5, 3) returns 8
        calculator("multiply", 4, 2) returns 8
    """
    if operation == "add":
        return a + b
    elif operation == "subtract":
        return a - b
    elif operation == "multiply":
        return a * b
    elif operation == "divide":
        return a / b if b != 0 else "Error: Division by zero"
    else:
        return "Error: Invalid operation"
    
@function_tool
def weather_checker(city: str) -> str:
    """A weather information tool that provides current weather conditions for major cities.
    
    This tool returns simulated weather data for predefined cities. It provides temperature
    and weather condition information in a human-readable format.
    
    Args:
        city (str): The name of the city to check weather for. Currently supports:
            - New York
            - London
            - Tokyo
            - Paris
    
    Returns:
        str: A string containing the weather information in the format "Condition, Temperature°C"
             Returns "Weather data not available for this city" if the city is not in the database
    
    Example:
        weather_checker("London") returns "Rainy, 15°C"
        weather_checker("Tokyo") returns "Cloudy, 20°C"
    """
    weather_data = {
        "New York": "Sunny, 25°C",
        "London": "Rainy, 15°C",
        "Tokyo": "Cloudy, 20°C",
        "Paris": "Clear, 22°C"
    }
    return weather_data.get(city, "Weather data not available for this city")

@function_tool
def unit_converter(value: float, from_unit: str, to_unit: str) -> str:
    """A simple unit converter tool that converts between common units of measurement.
    
    This tool converts values between different units of measurement like length, weight, and temperature.
    
    Args:
        value (float): The value to convert
        from_unit (str): The unit to convert from. Supported units:
            - Length: "km", "m", "cm", "inch", "ft"
            - Weight: "kg", "g", "lb", "oz"
            - Temperature: "c", "f"
        to_unit (str): The unit to convert to (same options as from_unit)
    
    Returns:
        str: The converted value with unit, or an error message if conversion is not supported
    
    Example:
        unit_converter(1, "km", "m") returns "1000.0 m"
        unit_converter(32, "f", "c") returns "0.0 c"
    """
    # Length conversions (to meters)
    length_to_m = {
        "km": 1000,
        "m": 1,
        "cm": 0.01,
        "inch": 0.0254,
        "ft": 0.3048
    }
    
    # Weight conversions (to kilograms)
    weight_to_kg = {
        "kg": 1,
        "g": 0.001,
        "lb": 0.453592,
        "oz": 0.0283495
    }
    
    # Check if it's a length conversion
    if from_unit in length_to_m and to_unit in length_to_m:
        meters = value * length_to_m[from_unit]
        result = meters / length_to_m[to_unit]
        return f"{result:.1f} {to_unit}"
    
    # Check if it's a weight conversion
    elif from_unit in weight_to_kg and to_unit in weight_to_kg:
        kg = value * weight_to_kg[from_unit]
        result = kg / weight_to_kg[to_unit]
        return f"{result:.1f} {to_unit}"
    
    # Temperature conversion
    elif from_unit == "c" and to_unit == "f":
        return f"{(value * 9/5) + 32:.1f} f"
    elif from_unit == "f" and to_unit == "c":
        return f"{(value - 32) * 5/9:.1f} c"
    
    else:
        return "Error: Unsupported unit conversion"

agent = Agent(
    name="Assistant", 
    instructions="You are a helpful assistant.", 
    tools=[calculator, weather_checker, unit_converter],
    # tool_use_behavior="stop_on_first_tool"
    tool_use_behavior={"stop_at_tool_names": ["calculator", "weather_checker", "unit_converter"]}
    # tool_use_behavior=StopAtTools(stop_at_tool_names=["calculator", "weather_checker", "unit_converter"])     # This is not the correct way because it's still making the dict behind the scene not the object (TypedDict)
)

# input = "What is the weather in newyork?"
# input = "What is 2 + 2?"
input = "Convert 5 kilometers to meters"
result = Runner.run_sync(agent, input, run_config=config)

print("=============================")
print(result.final_output)

# input = "Who is the founder of Pakistan?"