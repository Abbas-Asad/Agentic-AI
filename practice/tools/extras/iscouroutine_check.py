import inspect

async def add(a: int, b: int, c: int = 9) -> int:
    return a + b + c

def sub(a: int, b: int, c: int = 9) -> int:
    return a + b + c

print(f"iscoroutinefunction: {inspect.iscoroutinefunction(add)}")
print(f"iscoroutinefunction: {inspect.iscoroutinefunction(sub)}")