# Operators in Python
# +, -, *, /, %, **, //, =, +=, -=, *=, /=, %=, **=, //=, ==, !=, >, <, >=, <=, and, or, not, in, not in, is, is not

# Arithmetic Operators
a = 10
b = 20

print(a + b) # 30

print(a - b) # -10

print(a * b) # 200

print(a / b) # 0.5

print(a % b) # 10

print(a ** b) # 100000000000000000000

print(a // b) # 0

# Assignment Operators
a = 10
b = 20

a += b
print(a) # 30

a -= b
print(a) # 10

a *= b
print(a) # 200

a /= b
print(a) # 10.0

a %= b
print(a) # 10.0

a **= b
print(a) # 100000000000000000000

a //= b
print(a) # 4768371582031250

# Comparison Operators
a = 10
b = 20

print(a == b) # False

print(a != b) # True

print(a > b) # False

print(a < b) # True

print(a >= b) # False

print(a <= b) # True

# Logical Operators
a = True
b = False

print(a and b) # False

print(a or b) # True

print(not a) # False

# Membership Operators

a = "Hello World"
b = {1: "a", 2: "b"}

print("H" in a) # True

print("h" not in a) # True

print(1 in b) # True

print("a" in b) # False

# Identity Operators

a = 10
b = 10

print(a is b) # True

print(a is not b) # False

a = [1, 2, 3]
b = [1, 2, 3]

print(a is b) # False

print(a is not b) # True

# Bitwise Operators
a = 10
b = 20

print(a & b) # 0

print(a | b) # 30

print(a ^ b) # 30

print(~a) # -11

print(a << 2) # 40

print(a >> 2) # 2

# Order of Operations
a = 10
b = 20

print((a + b) * 10) # 300

print(a + (b * 10)) # 210

# Operator Precedence
# ** -> *, /, %, // -> +, - -> =, +=, -=, *=, /=, %=, **=, //= -> ==, !=, >, <, >=, <= -> and -> or -> not -> in, not in -> is, is not

# Operator Associativity

# Left to Right
a = 10
b = 20
c = 30

print(a + b + c) # 60

# Right to Left

print(a ** b ** c) # 100

# Operator Overloading
a = 10
b = 20

print(a + b) # 30

a = "Hello"
b = "World"

print(a + b) # HelloWorld

# Operator Overloading
a = 10
b = 20

print(a + b) # 30

a = "Hello"

b = "World"

print(a + b) # HelloWorld

# Operator Overloading

a = 10
b = 20

print(a + b) # 30

a = "Hello"
b = "World"

print(a + b) # HelloWorld

