# Module 06: Introduction to OOP in Python
# ----------------------------------------------------------------------------

# Introduction to Object-Oriented Programming (OOP)
# Object-Oriented Programming (OOP) is a programming paradigm that uses objects and classes to structure software. 
# A class is a blueprint for creating objects (instances), which are collections of attributes (variables) and methods (functions).

# 1. What is a Class?
# A class is a blueprint for creating objects. It defines a set of attributes and methods that the objects created from the class will have.

# Defining a Class
class Dog:
    # The __init__ method is the class constructor that initializes the object's attributes.
    def __init__(self, name, age, breed):
        self.name = name  # Attribute
        self.age = age    # Attribute
        self.breed = breed  # Attribute

    # Method
    def bark(self):
        return f"{self.name} says Woof!"

# Creating an Instance (Object) of the Class
my_dog = Dog("Buddy", 5, "Golden Retriever")
print("Dog's Name:", my_dog.name)      # Output: Dog's Name: Buddy
print("Dog's Age:", my_dog.age)        # Output: Dog's Age: 5
print("Dog's Breed:", my_dog.breed)    # Output: Dog's Breed: Golden Retriever
print(my_dog.bark())                   # Output: Buddy says Woof!

# 2. Understanding `self` and `__init__`
# The `self` Parameter:
# The `self` parameter is a reference to the current instance of the class and is used to access variables that belong to the class.
# It is the first parameter of any method in a class, including the `__init__` method. By convention, it is named `self`, but you could name it anything you like.

# Example:
# - When you create an object (e.g., `my_dog = Dog("Buddy", 5, "Golden Retriever")`), Python automatically passes the object itself as the first argument to the `__init__` method.
# - Inside the method, `self.name`, `self.age`, and `self.breed` refer to the attributes of the specific object being created or manipulated.

# The `__init__` Method:
# The `__init__` method is a special method in Python classes, known as the constructor. It is automatically called when a new object of the class is created.
# The primary purpose of `__init__` is to initialize the object's attributes with values when the object is created.

# Example:
# - In the `Dog` class, `__init__` takes `name`, `age`, and `breed` as parameters and assigns them to the object's attributes (`self.name`, `self.age`, `self.breed`).
# - This ensures that when you create a new `Dog` object, it starts with the attributes set to the values you provide.

# Class Example with `self` and `__init__`:
class Circle:
    def __init__(self, radius):
        self.radius = radius  # Instance attribute

    def area(self):
        return 3.14159 * (self.radius ** 2)  # Use self.radius to access the instance's radius

# Creating an instance of the Circle class
my_circle = Circle(5)
print("Circle's Area:", my_circle.area())  # Output: Circle's Area: 78.53975

# 3. Class Attributes and Methods
# Class attributes are shared across all instances of a class, while instance attributes are specific to each object. Methods are functions defined within a class.

class Circle:
    # Class attribute (shared by all instances)
    pi = 3.14159

    # Constructor (Instance attributes are unique to each object)
    def __init__(self, radius):
        self.radius = radius  # Instance attribute

    # Method to calculate the area of the circle
    def area(self):
        return Circle.pi * (self.radius ** 2)

# Creating instances of the Circle class
circle1 = Circle(5)
circle2 = Circle(10)

print("Circle 1 Area:", circle1.area())  # Output: Circle 1 Area: 78.53975
print("Circle 2 Area:", circle2.area())  # Output: Circle 2 Area: 314.159

# 4. Inheritance
# Inheritance allows you to create a new class based on an existing class. The new class (child class) inherits attributes and methods from the existing class (parent class).

# Example: 
# Let's consider an Animal class as the parent class and a Dog class as the child class.

class Animal:
    def __init__(self, name, species):
        self.name = name
        self.species = species

    def make_sound(self):
        return f"{self.name} makes a sound."

# Dog class inherits from Animal class
class Dog(Animal):
    def __init__(self, name, breed):
        # The super() function is used to call the constructor of the parent class (Animal).
        # This ensures that the attributes defined in the parent class are properly initialized.
        super().__init__(name, species="Dog")  
        self.breed = breed

    def bark(self):
        return f"{self.name} says Woof!"

# Creating an instance of Dog class
my_dog = Dog("Max", "Bulldog")
print("Dog's Name:", my_dog.name)            # Output: Dog's Name: Max
print("Dog's Species:", my_dog.species)      # Output: Dog's Species: Dog
print("Dog's Breed:", my_dog.breed)          # Output: Dog's Breed: Bulldog
print(my_dog.bark())                         # Output: Max says Woof!
print(my_dog.make_sound())                   # Output: Max makes a sound.

# Explanation of super():
# The `super()` function in Python is used to give you access to methods and properties of a parent class. 
# When used in the `__init__` method of a child class, it allows you to call the parent class's `__init__` method.
# This is important because it ensures that the parent class's attributes are properly initialized.

# In the example above:
# - `super().__init__(name, species="Dog")` calls the `__init__` method of the `Animal` class, passing the `name` and setting the `species` to "Dog".
# - This means that the `Dog` class automatically gets the attributes `name` and `species` from the `Animal` class, without needing to redefine them in the `Dog` class.
# - After calling `super().__init__`, the `Dog` class can add its own attributes (like `breed`) or override methods as needed.

# The `super()` function is a powerful tool in object-oriented programming because it allows you to extend and customize behavior in a child class 
# while still leveraging the functionality provided by a parent class.

# 5. Method Overriding
# Method overriding allows a child class to provide a specific implementation of a method that is already defined in its parent class.

class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name, species="Cat")
        self.breed = breed

    # Overriding the make_sound method
    def make_sound(self):
        return f"{self.name} says Meow!"

my_cat = Cat("Whiskers", "Siamese")
print(my_cat.make_sound())  # Output: Whiskers says Meow!

# 6. Encapsulation
# Encapsulation is the bundling of data (attributes) and methods that operate on the data into a single unit or class. 
# It also restricts direct access to some of an object's components.

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.__balance = balance  # Private attribute (prefix with double underscores)

    def deposit(self, amount):
        self.__balance += amount
        return f"Deposited {amount}. New balance is {self.__balance}."

    def withdraw(self, amount):
        if amount > self.__balance:
            return "Insufficient funds."
        self.__balance -= amount
        return f"Withdrew {amount}. New balance is {self.__balance}."

    def get_balance(self):
        return self.__balance

account = BankAccount("John")
print(account.deposit(100))       # Output: Deposited 100. New balance is 100.
print(account.withdraw(50))       # Output: Withdrew 50. New balance is 50.
print("Balance:", account.get_balance())  # Output: Balance: 50

# 7. Polymorphism
# Polymorphism allows you to use a single interface to represent different data types or classes. 
# In Python, this is often achieved through method overriding and duck typing.

class Bird:
    def make_sound(self):
        return "Tweet"

class Dog(Animal):
    def make_sound(self):
        return "Woof"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

# Polymorphism in action
def animal_sound(animal):
    print(animal.make_sound())

dog = Dog("Rex", "Labrador")
cat = Cat("Mittens", "Persian")
bird = Bird()

animal_sound(dog)   # Output: Woof
animal_sound(cat)   # Output: Meow
animal_sound(bird)  # Output: Tweet

# Practical Exercise
# Now it's your turn! Try to create a script that:
# 1. Defines a `Vehicle` class with attributes like `make`, `model`, and `year`.
# 2. Creates two child classes: `Car` and `Truck`, each with additional attributes and methods.
# 3. Demonstrates inheritance, method overriding, and encapsulation.
# 4. Creates instances of `Car` and `Truck` and calls their methods.

# Example:
class Vehicle:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year

    def get_info(self):
        return f"{self.year} {self.make} {self.model}"

class Car(Vehicle):
    def __init__(self, make, model, year, doors):
        super().__init__(make, model, year)
        self.doors = doors

    def get_info(self):
        return f"{super().get_info()} with {self.doors} doors"

class Truck(Vehicle):
    def __init__(self, make, model, year, capacity):
        super().__init__(make, model, year)
        self.capacity = capacity

    def get_info(self):
        return f"{super().get_info()} with {self.capacity} tons capacity"

my_car = Car("Toyota", "Corolla", 2020, 4)
my_truck = Truck("Ford", "F-150", 2019, 3)

print(my_car.get_info())  # Output: 2020 Toyota Corolla with 4 doors
print(my_truck.get_info())  # Output: 2019 Ford F-150 with 3 tons capacity

# Congratulations! You have completed the Introduction to Classes module in Python!