# Module 03: Functions in Python
# ----------------------------------------------------------------------------

# Introduction to Functions
# Functions are reusable blocks of code that perform a specific task. They help in organizing code, avoiding repetition, and improving readability.

# Defining a Function
# You define a function using the `def` keyword, followed by the function name and parentheses. The code block inside the function is executed when the function is called.

def greet(name):
    """This function prints a greeting message."""
    print("Hello, " + name + "!")

# Calling the Function
greet("Alice")  # Output: Hello, Alice!

# Function with Parameters
# Functions can accept parameters (inputs) and use them within the function. Parameters allow you to pass values to functions.

def add_numbers(a, b):
    """This function returns the sum of two numbers."""
    return a + b

# Calling the Function with Arguments
result = add_numbers(5, 3)
print("The sum is:", result)  # Output: The sum is: 8

# Function with Default Parameters
# You can provide default values for parameters. If no argument is passed for a parameter with a default value, the default value is used.

def multiply(x, y=1):
    """This function returns the product of two numbers. The second number has a default value of 1."""
    return x * y

print("Multiplication result (with default y):", multiply(4))        # Output: Multiplication result (with default y): 4
print("Multiplication result (with y=5):", multiply(4, 5))         # Output: Multiplication result (with y=5): 20

# Functions with Multiple Return Values
# Functions can return multiple values, which can be captured in multiple variables.

def get_person_info():
    """This function returns a tuple containing a name and an age."""
    return "Bob", 45

name, age = get_person_info()
print("Name:", name)  # Output: Name: Bob
print("Age:", age)    # Output: Age: 45

# Lambda Functions
# Lambda functions are small anonymous functions defined using the `lambda` keyword. They are useful for short, throwaway functions.

square = lambda x: x * x
print("Square of 5:", square(5))  # Output: Square of 5: 25

# Higher-Order Functions
# Functions that take other functions as arguments or return functions are called higher-order functions.

def apply_function(func, value):
    """This function applies a given function to a value."""
    return func(value)

print("Applying square function:", apply_function(square, 6))  # Output: Applying square function: 36

# Practical Exercise
# Now it's your turn! Try to create a script that:
# 1. Defines a function that takes a list of numbers and returns the average of those numbers.
# 2. Define another function that takes a string and returns the string in uppercase.
# 3. Use both functions to process user input.

# Tip: You can use the `sum()` function to calculate the sum of a list and the `upper()` method to convert a string to uppercase.

# Example:
def average(numbers):
    """This function returns the average of a list of numbers."""
    return sum(numbers) / len(numbers)

def to_uppercase(text):
    """This function returns the input string in uppercase."""
    return text.upper()

# Get user input and process it
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
text = input("Enter a string: ")

print("Average of numbers:", average(numbers))
print("Uppercase string:", to_uppercase(text))

# Congratulations! You have completed the Functions module in Python!