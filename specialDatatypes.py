# Immutable Datatypes: int, float, complex, bool, string, tuple, frozenset
# Mutable Datatypes: list, dict, set

# Special Datatypes

# 1. List
# List is a collection which is ordered and changeable. Allows duplicate members and it also allows multiple datatypes.
# List is represented by square brackets []

list = [1, 2, 3, 4, 5, 'Hello']

# List
l = [1, 2, 3, 4, 5]
print(l) # [1, 2, 3, 4, 5]

# Accessing List
print(l[0]) # 1
print(l[1]) # 2

# Negative Indexing
print(l[-1]) # 5
print(l[-2]) # 4

# Slicing
print(l[0:3]) # [1, 2, 3]

# Change Item Value
l[0] = 10
print(l) # [10, 2, 3, 4, 5]

# Add Item
l.append(6)
print(l) # [10, 2, 3, 4, 5, 6]

# Insert Item
l.insert(1, 20)
print(l) # [10, 20, 2, 3, 4, 5, 6]

# Remove Item
l.remove(20)
print(l) # [10, 2, 3, 4, 5, 6]

# Pop Item
l.pop()
print(l) # [10, 2, 3, 4, 5]

# Clear List
l.clear()
print(l) # []

# join List

l1 = [1, 2, 3]
l2 = [4, 5, 6]

l3 = l1 + l2
print(l3) # [1, 2, 3, 4, 5, 6]

# 2. Tuple
# Tuple is a collection which is ordered and unchangeable. Allows duplicate members. It can also have multiple datatypes.
# Tuple is represented by round brackets ()

tuple = (1, 2, 3, 4, 5, 'Hello')

# Tuple
t = (1, 2, 3, 4, 5)
print(t) # (1, 2, 3, 4, 5)

# Accessing Tuple
print(t[0]) # 1
print(t[1]) # 2

# Negative Indexing
print(t[-1]) # 5
print(t[-2]) # 4

# Slicing
print(t[0:3]) # (1, 2, 3)

# Change Item Value
# t[0] = 10 # TypeError: 'tuple' object does not support item assignment

#convert tuple to list
l = list(t)
print(l) # [1, 2, 3, 4, 5]

#convert list to tuple
t = tuple(l)
print(t) # (1, 2, 3, 4, 5)

# 3. Set
# Set is a collection which is unordered and unindexed. No duplicate members.

# Set
s = {1, 2, 3, 4, 5}
print(s) # {1, 2, 3, 4, 5}

# Accessing Set

# print(s[0]) # TypeError: 'set' object is not subscriptable

# Add Item
s.add(6)
print(s) # {1, 2, 3, 4, 5, 6}

# Remove Item
s.remove(6)
print(s) # {1, 2, 3, 4, 5}

#convert set to list
l = list(s)
print(l) # [1, 2, 3, 4, 5]

#convert list to set
s = set(l)
print(s) # {1, 2, 3, 4, 5}

# Clear Set
s.clear()
print(s) # set()

# 4. Dictionary

# Dictionary is a collection which is unordered, changeable and indexed. No duplicate members.
# Dictionary is represented by curly brackets {}

# Dictionary
d = {
    "name": "John",
    "age": 30,
    "city": "New York"
}

print(d) # {'name': 'John', 'age': 30, 'city': 'New York'}

# Accessing Dictionary
print(d["name"]) # John
print(d["age"]) # 30

# Change Item Value
d["name"] = "Doe"

print(d) # {'name': 'Doe', 'age': 30, 'city': 'New York'}

# Add Item
d["country"] = "USA"
print(d) # {'name': 'Doe', 'age': 30, 'city': 'New York', 'country': 'USA'}

# Remove Item
d.pop("city")
print(d) # {'name': 'Doe', 'age': 30, 'country': 'USA'}

# Clear Dictionary
d.clear()
print(d) # {}

# 5. Range
# Range is a collection which is ordered and immutable. Allows duplicate members.
# Range is represented by range() function

# Range
r = range(6)
print(r) # range(0, 6)

# Accessing Range
print(r[0])
print(r[1])

# Negative Indexing
print(r[-1]) # 5
print(r[-2]) # 4

# Slicing
print(r[0:3]) # range(0, 3)

# Change Item Value
# r[0] = 10 # TypeError: 'range' object does not support item assignment

# 6. Frozenset
# Frozenset is a collection which is unordered and unchangeable. No duplicate members.
# Frozenset is represented by frozenset() function

# Frozenset
fs = frozenset({1, 2, 3, 4, 5})
print(fs) # frozenset({1, 2, 3, 4, 5})

# Accessing Frozenset

# print(fs[0]) # TypeError: 'frozenset' object is not subscriptable

# Add Item
# fs.add(6) # AttributeError: 'frozenset' object has no attribute 'add'

# Remove Item
# fs.remove(6) # AttributeError: 'frozenset' object has no attribute 'remove'

# 7. Bytes
# Bytes is a collection which is immutable. Allows duplicate members.

# Bytes
b = b"Hello"

print(b) # b'Hello'

# Accessing Bytes
print(b[0]) # 72
print(b[1]) # 101

# Negative Indexing

print(b[-1]) # 111

# Slicing
print(b[0:3]) # b'Hel'

# Change Item Value
# b[0] = 10 # TypeError: 'bytes' object does not support item assignment

# 8. Bytearray
# Bytearray is a collection which is mutable. Allows duplicate members.
