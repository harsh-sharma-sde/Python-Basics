# print function 

print ("Hello World")
print ("Hello" + "World") # Concatenation
print (2 + 3) # Addition

# DataTypes

# String : "Hello World" -> str
# Integer : 2, 3, 4 -> int
# Float : 2.3, 3.4, 4.5 -> float
# Boolean : True, False -> bool
# Complex : 2 + 3j -> complex

print(type("Hello World")) # <class 'str'>
print(type(2)) # <class 'int'>
print(type(2.3)) # <class 'float'>
print(type(True)) # <class 'bool'>
print(type(2 + 3j)) # <class 'complex'>

# Variables & Constants
# Variables : A variable is a container for storing data values.
# Constants : A constant is a type of variable which value cannot be changed.

# Variables
x = 5
print(x) # 5

a, b, c = 5, 3.2, "Hello"
print(a) # 5
print(b) # 3.2
print(c) # Hello

x = y = z = "Hello"
print(x) # Hello

# Constants
PI = 3.14
print(PI) # 3.14

# input function
name = input("Enter your name: ")
print("Hello " + name)

# Input function always return a string

# Type Casting
# x = int(input("Enter a number: "))

x = 5.88
print(int(x)) # 5

print('Hello' * 3) # HelloHelloHello

# Slicing
# string[start:end:step]

s = "Hello World"
print(s[0]) # H
print(s[0:5]) # Hello

# String Methods
# len() : Returns the length of the string
# lower() : Converts a string into lower case
# upper() : Converts a string into upper case
# replace() : Replaces a string with another string
# split() : Splits the string into substrings if it finds instances of the separator

s = "Hello"
y = "World"
print(s + " " + y) # Hello World
print(len(s)) # 5
print(s.lower()) # hello
print(s.upper()) # HELLO
print(s.replace("H", "J")) # Jello
print(s.split("e")) # ['H', 'llo']


