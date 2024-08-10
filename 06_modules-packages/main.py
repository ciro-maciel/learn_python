# Module 06: Modules and Packages in Python
# ----------------------------------------------------------------------------

# Introduction to Modules and Packages
# In Python, modules and packages are used to organize and reuse code. A module is simply a file containing Python definitions and statements, while a package is a collection of modules in a directory that gives structure and organization to the codebase.

# Importing Modules
# You can import a module using the `import` keyword, allowing you to use its functions, classes, and variables.

# 1. Importing a Built-in Module
# Python comes with many built-in modules, such as `math`, `random`, and `datetime`.

import math

# Using functions from the math module
print("Square root of 16:", math.sqrt(16))
print("Pi constant:", math.pi)

# 2. Importing Specific Functions from a Module
# You can import specific functions or variables from a module using the `from ... import ...` syntax.

from random import randint, choice

# Using imported functions
print("Random integer between 1 and 10:", randint(1, 10))
print("Random choice from a list:", choice(["apple", "banana", "cherry"]))

# 3. Renaming Modules with `as`
# You can give a module or function a different name when importing it using the `as` keyword.

import datetime as dt

# Using the alias
now = dt.datetime.now()
print("Current date and time:", now)

# Creating Your Own Module
# You can create your own module by writing Python code in a `.py` file and importing it into other scripts.

# You can import and use your custom module like this:
import mymodule
from mymodule import greet

# Using functions from the custom module
print(greet("Alice"))
print("Sum:", mymodule.add(5, 7))

# Using classes from the custom module
calculator = mymodule.Calculator("Casio")
print("Multiplication:", calculator.multiply(3, 4))
print("Calculator brand:", calculator.brand)

# Packages
# A package is a way of organizing related modules into a directory hierarchy. Each package in Python is a directory containing a special `__init__.py` file (which can be empty).

# 1. Creating a Package
# To create a package, create a directory with an `__init__.py` file. Inside this directory, you can place multiple modules.

# Example Package Structure:
# mypackage/
# ├── __init__.py
# ├── module1.py
# └── module2.py

# You can import classes from these modules as follows:
from mypackage.module1 import Circle
from mypackage.module2 import Rectangle

# Using classes from the package modules
circle = Circle(5)
rectangle = Rectangle(4, 6)

print("Area of the circle:", circle.area())
print("Area of the rectangle:", rectangle.area())

# 2. Importing Everything from a Module
# You can import everything from a module using the `from ... import *` syntax. However, it's generally better to avoid this to keep your namespace clean.

from math import *

print("Cosine of 0 degrees:", cos(0))
print("Natural logarithm of e:", log(math.e))

# Practical Exercise
# Now it's your turn! Try to create a script that:
# 1. Creates a custom module with a few functions and a class, and imports them into a separate script.
# 2. Creates a package with at least two modules, each containing a class, and imports them into a script to demonstrate their usage.
# 3. Uses a built-in module to perform some operations (e.g., `math`, `random`, `datetime`).

# Tip: You can organize your code by placing custom modules and packages in the same directory as your main script.

# Example:
# 1. Create a module `calculator.py` with functions for addition, subtraction, multiplication, and division, and a class for a more advanced calculator.
# 2. Create a package `shapes` with modules for calculating the area of different shapes (e.g., `circle.py`, `rectangle.py`).
# 3. Write a script to use these modules and packages to perform various calculations.

# Example for custom module and class usage:
# ----------------------------------------------------------------------------
# # calculator.py
# def add(x, y):
#     return x + y
# 
# def subtract(x, y):
#     return x - y
# 
# def multiply(x, y):
#     return x * y
# 
# def divide(x, y):
#     if y == 0:
#         return "Cannot divide by zero!"
#     return x / y
#
# class AdvancedCalculator:
#     def power(self, base, exponent):
#         return base ** exponent
# 
#     def square_root(self, number):
#         return math.sqrt(number)
# ----------------------------------------------------------------------------

### UNCOMMENT THE CODE BELOW ###

# import calculator

# print("Addition:", calculator.add(10, 5))
# print("Subtraction:", calculator.subtract(10, 5))
# print("Multiplication:", calculator.multiply(10, 5))
# print("Division:", calculator.divide(10, 0))

# adv_calc = calculator.AdvancedCalculator()
# print("Power:", adv_calc.power(2, 3))
# print("Square Root:", adv_calc.square_root(16))

### UNCOMMENT THE CODE ABOVE ###

# Congratulations! You have completed the Modules and Packages module in Python!
