# Module 05: Modules and Packages in Python
# ----------------------------------------------------------------------------

# Introduction to Modules and Packages
# Modules and packages help in organizing and structuring your Python code. Modules are individual files containing Python code, while packages are collections of modules organized in directories.

# 1. What is a Module?
# A module is a file containing Python definitions and statements. The filename is the module name with the suffix `.py` added.

# Importing a Module
# You can import a module using the `import` statement.

import mymodule

mymodule.greet("Alice")  # Output: Hello, Alice!
result = mymodule.add_numbers(5, 3)
print("The sum is:", result)  # Output: The sum is: 8

# 2. Importing Specific Functions
# Instead of importing the whole module, you can import specific functions or variables.

from mymodule import greet, add_numbers

greet("Bob")  # Output: Hello, Bob!
result = add_numbers(10, 20)
print("The sum is:", result)  # Output: The sum is: 30

# 3. Aliases
# You can give a module or function an alias using the `as` keyword.

import mymodule as mm

mm.greet("Charlie")  # Output: Hello, Charlie!

from mymodule import add_numbers as add
result = add(7, 8)
print("The sum is:", result)  # Output: The sum is: 15

# 4. What is a Package?
# A package is a collection of modules organized in directories. Each directory contains an `__init__.py` file, which can be empty or contain initialization code for the package.

# Example Package Structure:
# mypackage/
# ├── __init__.py
# ├── module1.py
# └── module2.py

# Importing from a Package
# You can import modules or functions from a package using the dot notation.

from mypackage import module1, module2

module1.greet("Alice")  # Output: Hello from module1, Alice!
module2.farewell("Bob")  # Output: Goodbye from module2, Bob!

# Importing Specific Functions from a Module in a Package
# You can also import specific functions directly from modules within a package.

from mypackage.module1 import greet
greet("Charlie")  # Output: Hello from module1, Charlie!

# Practical Exercise
# Now it's your turn! Try to create a script that:
# 1. Creates a module with at least two functions.
# 2. Creates a package with at least two modules.
# 3. Imports and uses functions from the module and the package in a separate script.

# Example Module and Package Creation:

### UNCOMMENT THE CODE BELOW ###

# # Save the following code as `my_module.py`.
# def square(number):
#     """This function returns the square of a number."""
#     return number * number

# # Save the following code as `my_package/__init__.py` (can be empty).

# # Save the following code as `my_package/module_a.py`.
# def cube(number):
#     """This function returns the cube of a number."""
#     return number * number * number

# # Save the following code as `my_package/module_b.py`.
# def double(number):
#     """This function returns double of a number."""
#     return number * 2

# # Save the following code as `main_script.py`.
# import my_module
# from my_package import module_a, module_b

# print("Square of 4:", my_module.square(4))  # Output: Square of 4: 16
# print("Cube of 3:", module_a.cube(3))       # Output: Cube of 3: 27
# print("Double of 5:", module_b.double(5))   # Output: Double of 5: 10

### UNCOMMENT THE CODE ABOVE ###

# Congratulations! You have completed the Modules and Packages module in Python!
