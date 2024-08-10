# Module 04: Flow Control in Python
# ----------------------------------------------------------------------------

# Introduction to Flow Control
# Flow control statements allow you to control the execution of code based on certain conditions or to repeat code multiple times. Python provides several constructs for flow control, including conditional statements and loops.

# Conditional Statements
# Conditional statements are used to execute different blocks of code based on certain conditions.

# 1. If Statement
age = 18
if age >= 18:
    print("You are an adult.")

# 2. If-Else Statement
temperature = 25
if temperature > 30:
    print("It's a hot day.")
else:
    print("It's a pleasant day.")

# 3. If-Elif-Else Statement
score = 85
if score >= 90:
    print("Grade: A")
elif score >= 80:
    print("Grade: B")
elif score >= 70:
    print("Grade: C")
else:
    print("Grade: D")

# 4. Nested If Statements
number = 15
if number % 2 == 0:
    if number % 4 == 0:
        print("The number is even and divisible by 4.")
    else:
        print("The number is even but not divisible by 4.")
else:
    print("The number is odd.")

# Simulating Switch with Dictionaries
# Python does not have a switch statement, but you can simulate it using dictionaries.

def switch_case(option):
    switch = {
        "a": "Option A selected",
        "b": "Option B selected",
        "c": "Option C selected",
    }
    return switch.get(option, "Invalid option")

print(switch_case("b"))  # Output: Option B selected
print(switch_case("x"))  # Output: Invalid option

# Ternary Conditional Expression
# The ternary conditional expression allows you to write simple if-else statements in a single line.

is_even = "Even" if number % 2 == 0 else "Odd"
print("The number is:", is_even)

# Loops
# Loops are used to execute a block of code repeatedly until a certain condition is met.

# 1. For Loop
colors = ["red", "green", "blue"]
for color in colors:
    print("Color:", color)

# 2. While Loop
count = 0
while count < 5:
    print("Count:", count)
    count += 1

# 3. Break Statement
for i in range(10):
    if i == 5:
        break
    print("i:", i)

# 4. Continue Statement
for i in range(10):
    if i % 2 == 0:
        continue
    print("Odd number:", i)

# 5. Pass Statement
for i in range(5):
    if i == 3:
        pass  # Placeholder for future code
    print("Number:", i)

# Handling Exceptions
# Use try-except blocks to handle exceptions and manage control flow in the presence of errors.

try:
    result = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero!")

# List Comprehensions with Conditional Logic
# List comprehensions provide a concise way to create lists based on existing lists with conditions.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [num for num in numbers if num % 2 == 0]
print("Even numbers:", even_numbers)

# Practical Exercise
# Now it's your turn! Try to create a script that:
# 1. Asks the user to enter a number and determines if the number is positive, negative, or zero.
# 2. Uses a `for` loop to print the squares of numbers from 1 to 10.
# 3. Uses a `while` loop to sum numbers until the user decides to stop.
# 4. Simulates a switch statement to perform different actions based on user input.
# 5. Uses a ternary conditional expression to print a message indicating if a number is even or odd.

# Example:
number = int(input("Enter a number: "))
if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    print("The number is zero.")

print("\nSquares of numbers from 1 to 10:")
for i in range(1, 11):
    print(i * i)

print("\nSum of numbers. Type 'stop' to end.")
total_sum = 0
while True:
    user_input = input("Enter a number to add (or type 'stop' to finish): ")
    if user_input.lower() == 'stop':
        break
    try:
        total_sum += int(user_input)
    except ValueError:
        print("Please enter a valid number.")
print("Total sum:", total_sum)

# Simulate a switch case
option = input("Choose an option (a, b, c): ")
print(switch_case(option))

# Ternary conditional example
even_or_odd = "Even" if number % 2 == 0 else "Odd"
print(f"The number is {even_or_odd}.")

# Congratulations! You have completed the Flow Control module in Python!
