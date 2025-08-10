# ❌ No, you cannot do this at the top level in a Python script:
# python
# Copy
# Edit
# first_function()  # ❌ This will raise NameError

# def first_function():
#     print("Executing first function.")
# ❗Why?
# When Python executes a script, it runs top to bottom. So:

# At the moment it hits first_function(), the function has not yet been defined.

# This leads to a NameError: name 'first_function' is not defined.

# ✅ But you can do it inside a class or another function:
# Why does it work in the Runner class?

# Because the method _run_single_turn isn't called at the time the class is defined — it's called later, when Runner.run() is actually executed at runtime.

# Here’s a simplified version that works:

# python
# Copy
# Edit
# class MyClass:
#     @classmethod
#     def main(cls):
#         cls.hello()  # ✅ Okay, because it's called at runtime

#     @classmethod
#     def hello(cls):
#         print("Hello!")

# MyClass.main()  # Triggers everything
# ✅ Or inside a function:
# python
# Copy
# Edit
# def main():
#     first_function()  # ✅ OK, because this line runs after the definition below

# def first_function():
#     print("It works!")

# main()
# 🧠 Rule of Thumb:
# Top-level calls need the function to be defined before the call.

# Runtime calls (inside other functions/classes) can refer to methods/functions defined later in the code.

# Let me know if you'd like a visual explanation or code trace!