# Module 02: Introduction to Variables and Data Types in Python
# ----------------------------------------------------------------------------

# What are variables?
# In Python, a variable is a name that refers to a value. Variables are used to store information that can be used and manipulated later in the code.

# Examples of variables:
name = "John"        # String
age = 30            # Integer
height = 1.75       # Float (floating-point number)
is_student = True   # Boolean

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is student?", is_student)

# Data Types

# 1. String Type (str)
# Strings are sequences of characters. In Python, you can create a string using single or double quotes.
message = "Hello, World!"
print("Message:", message)

# 2. Integer Type (int)
# Integers are whole numbers without a decimal point.
number = 42
print("Number:", number)

# 3. Float Type (float)
# Floats are numbers with a decimal point.
pi = 3.14159
print("Pi:", pi)

# 4. Boolean Type (bool)
# Booleans represent logical values: True or False.
true_value = True
false_value = False
print("True:", true_value)
print("False:", false_value)

# 5. Dictionary Type (dict)
# Dictionaries are collections of key-value pairs. They are useful for storing data that needs to be accessed by a specific key.
person = {
    "name": "Maria",
    "age": 28,
    "height": 1.65,
    "is_student": False
}

# Accessing values in a dictionary
print("Person's name:", person["name"])
print("Person's age:", person["age"])

# Adding and Updating Values
person["city"] = "São Paulo"  # Adds a new key-value pair
person["age"] = 29            # Updates the value of the key "age"
print("Updated person:", person)

# Removing an Item
del person["city"]
print("Person without 'city' key:", person)

# Variable Operations
# You can perform mathematical operations and string concatenation with variables.

# 6. Mathematical Operations
addition = 5 + 3
subtraction = 10 - 2
multiplication = 4 * 3
division = 12 / 4
print("Addition:", addition)
print("Subtraction:", subtraction)
print("Multiplication:", multiplication)
print("Division:", division)

# 7. Concatenating Strings
full_name = name + " Silva"
print("Full Name:", full_name)

# Data Types and Conversions
# Sometimes you might need to convert one data type to another.
number_as_str = str(number)  # Converts integer to string
print("Number as String:", number_as_str)

# 8. Checking Data Types
print("Type of name:", type(name))
print("Type of age:", type(age))
print("Type of height:", type(height))
print("Type of is_student:", type(is_student))
print("Type of person:", type(person))

# 9. Practical Exercise
# Now it's your turn! Try to create a script that:
# 1. Asks the user for their favorite color and their birth year.
# 2. Calculates the user's age based on the current year (assume the current year is 2024).
# 3. Prints a message that includes the user's favorite color and their age.

# Tip: You can use the `input()` function to capture user input and the `int()` function to convert strings to integers.

# Example:
favorite_color = input("What is your favorite color? ")
birth_year = int(input("What is your birth year? "))
current_year = 2024
age = current_year - birth_year
print("Your favorite color is " + favorite_color + " and you are " + str(age) + " years old.")

# Congratulations! You have completed the Introduction to Variables and Data Types in Python!