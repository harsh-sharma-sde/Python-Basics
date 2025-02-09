# loops in python


# for loop
for i in range(5):
    print(i) # 0 1 2 3 4

# for loop with start and end
for i in range(2, 5):
    print(i) # 2 3 4

# for loop with start, end and step

for i in range(2, 10, 2):
    print(i) # 2 4 6 8

# for loop with negative step
for i in range(10, 2, -2):
    print(i) # 10 8 6 4

# for loop with list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit) # apple banana cherry

# for loop with string
for char in "Hello":
    print(char) # H e l l o

# while loop
i = 0
while i < 5:
    print(i)
    i += 1 # 0 1 2 3 4

# while loop with break
i = 0
while i < 5:
    print(i)
    if i == 3:
        break
    i += 1 # 0 1 2 3

# while loop with continue
i = 0
while i < 5:
    i += 1
    if i == 3:
        continue
    print(i) # 1 2 4 5

# while loop with else
i = 0
while i < 5:
    print(i)
    i += 1

else:
    print("i is no longer less than 5") # 0 1 2 3 4 i is no longer less than 5

# nested loop
for i in range(2):
    for j in range(2):
        print(i, j) # 0 0 0 1 1 0 1 1

# pass statement
for i in range(5):
    pass

