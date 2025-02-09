# functions in python

# defining a function
def greet():
    print("Hello, World!")

# calling a function
greet() # Hello, World!

# function with arguments
def greet(name):
    print("Hello, " + name)

greet("John") # Hello, John

# function with return statement
def add(a, b):
    return a + b

result = add(2, 3)

print(result) # 5

# function with default arguments

def greet(name = "World"):
    print("Hello, " + name)

greet() # Hello, World
greet("John") # Hello, John

# function with keyword arguments

def greet(name, msg):
    print("Hello, " + name + ", " + msg)

greet(name = "John", msg = "Good Morning") # Hello, John, Good Morning

# function with variable length arguments

def greet(*names):
    for name in names:
        print("Hello, " + name)

greet("John", "Jane", "Doe") # Hello, John Hello, Jane Hello, Doe

# function with variable length keyword arguments

def greet(**names):
    for key, value in names.items():
        print(key, value)

greet(name1 = "John", name2 = "Jane", name3 = "Doe") # name1 John name2 Jane name3 Doe

# lambda function

add = lambda a, b: a + b

print(add(2, 3)) # 5

# map function

def square(x):
    return x * x

numbers = [1, 2, 3, 4, 5]

squared = map(square, numbers)

print(list(squared)) # [1, 4, 9, 16, 25]

# filter function

def is_even(x):
    return x % 2 == 0

numbers = [1, 2, 3, 4, 5]

even = filter(is_even, numbers)

print(list(even)) # [2, 4]

# reduce function

from functools import reduce

def add(a, b):
    return a + b

numbers = [1, 2, 3, 4, 5]

sum = reduce(add, numbers)


print(sum) # 15

# recursion

def factorial(n):
    if n == 0:
        return 1
    return n * factorial(n - 1)

print(factorial(5)) # 120

# decorators

def decorator(func):
    def wrapper():
        print("Before calling the function")
        func()
        print("After calling the function")
    return wrapper

@decorator
def greet():
    print("Hello, World!")

greet()

# Before calling the function
# Hello, World!
# After calling the function

# generators

def square(n):
    for i in range(n):
        yield i * i

squared = square(5)

print(list(squared)) # [0, 1, 4, 9, 16]

# generator expression

squared = (i * i for i in range(5))

print(list(squared)) # [0, 1, 4, 9, 16]

# generator with next function

def square(n):
    for i in range(n):
        yield i * i

squared = square(5)

print(next(squared)) # 0

print(next(squared)) # 1

print(next(squared)) # 4

print(next(squared)) # 9

print(next(squared)) # 16

# exception handling

try:
    print(x)
except:
    print("An exception occurred")

# An exception occurred

# try-except-else

try:
    print("Hello, World!")
except:
    print("An exception occurred")

else:
    print("No exception occurred")

# Hello, World!
# No exception occurred

# try-except-finally

try:
    print(x)
except:
    print("An exception occurred")
finally:
    print("The 'try except' is finished")

# An exception occurred
# The 'try except' is finished

# raise an exception

x = -1

if x < 0:
    raise Exception("Sorry, no numbers below zero")

# Exception: Sorry, no numbers below zero

# assert statement

x = 1

assert x > 0, "Invalid number"

print("Number is positive")

# Number is positive

# file handling

# write to a file

f = open("file.txt", "w")
f.write("Hello, World!")
f.close()

# read from a file

f = open("file.txt", "r")
print(f.read())
f.close()

# Hello, World!

# with statement

with open("file.txt", "w") as f:
    f.write("Hello, World!")

with open("file.txt", "r") as f:
    print(f.read())

# Hello, World!

# classes and objects

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print("Hello, my name is " + self.name)

person = Person("John", 36)

print(person.name) # John
print(person.age) # 36
person.greet() # Hello, my name is John

# inheritance

class Student(Person):
    def __init__(self, name, age, rollno):
        super().__init__(name, age)
        self.rollno = rollno

    def study(self):
        print("I am studying")

student = Student("Jane", 20, 101)

print(student.name) # Jane
print(student.age) # 20
print(student.rollno) # 101
student.greet() # Hello, my name is Jane
student.study() # I am studying

# operator overloading

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __str__(self):
        return f"({self.x}, {self.y})"
    
p1 = Point(2, 3)
p2 = Point(-1, 2)

print(p1 + p2) # (1, 5)

# method overloading

class Calculator:
    def add(self, a, b):
        return a + b

    def add(self, a, b, c):
        return a + b + c
    
calc = Calculator()

print(calc.add(2, 3)) # TypeError: add() missing 1 required positional argument: 'c'
print(calc.add(2, 3, 4)) # 9

# method overriding

class Animal:
    def speak(self):
        print("Animal is speaking")

class Dog(Animal):
    def speak(self):
        print("Dog is barking")

dog = Dog()

dog.speak() # Dog is barking

# data hiding

class Person:
    def __init__(self, name, age):
        self._name = name
        self.__age = age

    def display(self):
        print("Name:", self._name)
        print("Age:", self.__age)

person = Person("John", 36)

person.display()

print(person._name) # John
print(person.__age) # AttributeError: 'Person' object has no attribute '__age'

# encapsulation

class Person:
    def __init__(self):
        self.__name = None

    def set_name(self, name):
        self.__name = name

    def get_name(self):
        return self.__name
    
person = Person()

person.set_name("John")

print(person.get_name()) # John

# polymorphism

class Dog:
    def speak(self):
        print("Dog is barking")

class Cat:
    def speak(self):
        print("Cat is meowing")

def speak(animal):
    animal.speak()

dog = Dog()
cat = Cat()

speak(dog) # Dog is barking
speak(cat) # Cat is meowing

# magic methods

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)
    
p1 = Point(2, 3)
p2 = Point(-1, 2)

print(p1 + p2) # (1, 5)

# modules

# import module
import math

print(math.sqrt(16)) # 4.0

# import module with alias

import math as m

print(m.sqrt(16)) # 4.0

# from module import function

from math import sqrt

print(sqrt(16)) # 4.0

# from module import function with alias

from math import sqrt as s

print(s(16)) # 4.0

# import all functions from module

from math import *

print(sqrt(16)) # 4.0