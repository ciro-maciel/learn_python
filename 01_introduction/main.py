# Module 01: Introduction to Python
# ----------------------------------------

# 1. What is Python?
# Python is a high-level programming language widely used for automation, data analysis, web development, and more.
# Its simplicity and versatility make it one of the most popular languages in the world.

# Let's start with a simple program that prints a message on the screen.

# Basic example:
print("Hello, World!")

# This is known as "Hello, World!" - the first program many developers write.

# 2. Interacting with Python
# Python can be executed in various ways:
# 1. In the terminal/interactive interpreter (REPL).
# 2. By writing scripts in `.py` files.
# 3. Using interactive notebooks like Jupyter.

# Here, we are writing a script in a `.py` file.
# Let's see some basic examples of operations with Python.

# Example of a mathematical operation:
print("Sum of 2 + 3:", 2 + 3)

# We can also store values in variables:
a = 10
b = 5
print("Subtraction of a - b:", a - b)

# 3. Comments and Best Practices
# Comments are essential to make your code readable and understandable to others (and to yourself in the future).
# Anything you write after a `#` is ignored by Python.

# Comments in Python:
# This is a single-line comment.

"""
This is a multi-line comment.
It is useful for explaining more complex parts of the code or providing extensive documentation.
"""

# 4. Basic Data Types
# In Python, you don't need to explicitly declare the type of a variable.
# Let's explore some basic data types.

# Integer numbers:
integer = 10
print("Integer number:", integer)

# Decimal numbers (float):
decimal = 3.14
print("Decimal number (float):", decimal)

# Strings (sequence of characters):
text = "Hello, Python!"
print("String:", text)

# 5. Practical Exercise
# Now it's your turn! Try to create a script that:
# 1. Asks the user for their name and age.
# 2. Prints a personalized message with the provided name and age.

# Tip: You can use the `input()` function to capture user input.

# Example:
name = input("What is your name? ")
age = input("What is your age? ")
print("Hello, " + name + "! You are " + age + " years old.")

# Congratulations! You have completed the introduction to Python!