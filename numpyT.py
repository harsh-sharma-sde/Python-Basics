# numpy python module : numpy is a python module used for numerical computing

import numpy as np

# create a numpy array
a = np.array([1, 2, 3, 4, 5])
print(a)

# create a numpy array with range
b = np.arange(10)
print(b)

# npmpy array vs python list
# numpy array is faster than python list
# numpy array is memory efficient than python list
# numpy array is convenient than python list

# numpy array operations
# numpy array addition
a = np.array([1, 2, 3, 4, 5])
b = np.array([6, 7, 8, 9, 10])
c = a + b
print(c)

# numpy array subtraction
c = a - b
print(c)

# numpy array multiplication
c = a * b
print(c)

# numpy array division
c = a / b
print(c)

# numpy array dot product
c = np.dot(a, b)
print(c)

# numpy array sum
c = np.sum(a)
print(c)

# numpy array mean
c = np.mean(a)
print(c)

# numpy array max
c = np.max(a)
print(c)

# numpy array min
c = np.min(a)
print(c)

# numpy array reshape
a = np.array([1, 2, 3, 4, 5, 6])
b = a.reshape(2, 3)
print(b)

# numpy array transpose
c = b.T
print(c)

# type of numpy array
print(type(a)) # <class 'numpy.ndarray'> : Its a n dimensional array like matrix in cpp

# numpy array indexing
a = np.array([1, 2, 3, 4, 5])
print(a[0]) # 1

# numpy array slicing
a = np.array([1, 2, 3, 4, 5])
print(a[0:3]) # [1 2 3]

# numpy array 2D indexing
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a[0, 0]) # 1

# numpy array 2D slicing
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a[0:2, 0:2]) # [[1 2] [4 5]]

# numpy array 2D slicing
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a[0:2, 0:3]) # [[1 2 3] [4 5 6]]

# shape of numpy array
a = np.array([[1, 2, 3], [4, 5, 6]])
print(a.shape) # (2, 3) : 2 rows and 3 columns

# numpy array 3D indexing
a = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(a[0, 0, 0]) # 1

# numpy array 3D slicing
a = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(a[0:2, 0:2, 0:2]) # [[[1 2] [4 5]] [[7 8] [10 11]]]

# numpy array with data type
a = np.array([1, 2, 3, 4, 5], dtype=np.float32)
print(a) # [1. 2. 3. 4. 5.]

# numpy array with zeros
a = np.zeros((2, 3)) # 2 rows and 3 columns
print(a) # [[0. 0. 0.] [0. 0. 0.]] : 2D array

# numpy array with ones
a = np.ones((2, 3)) # 2 rows and 3 columns
print(a) # [[1. 1. 1.] [1. 1. 1.]] : 2D array

# numpy array with random numbers
a = np.random.random((2, 3)) # 2 rows and 3 columns
print(a) # [[0. 0. 0.] [0. 0. 0.]] : 2D array

# numpy array with specific number
a = np.full((2, 3), 5) # 2 rows and 3 columns
print(a) # [[5 5 5] [5 5 5]] : 2D array

# numpy array with identity matrix
a = np.eye(3) # 3x3 identity matrix
print(a) # [[1. 0. 0.] [0. 1. 0.] [0. 0. 1.]] : 3x3 identity matrix

# numpy array with diagonal matrix
a = np.diag([1, 2, 3]) # 3x3 diagonal matrix
print(a) # [[1 0 0] [0 2 0] [0 0 3]] : 3x3 diagonal matrix

# numpy array with linspace
a = np.linspace(1, 10, 5) # 5 numbers between 1 and 10
print(a) # [ 1.    3.25  5.5   7.75 10.  ] : 5 numbers between 1 and 10

# numpy array with arange
a = np.arange(1, 10, 2) # 1 to 10 with step 2
print(a) # [1 3 5 7 9] : 1 to 10 with step 2

# random number generation
a = np.random.randint(1, 10) # random number between 1 and 10
print(a) # 5 : random number between 1 and 10

# random number array generation with specific shape
a = np.random.randint(1, 10, (2, 3)) # 2x3 random number array between 1 and 10
print(a) # [[5 6 2] [6 6 4]] : 2x3 random number array between

# array with evenly spaced values
a = np.linspace(1, 10, 5) # 5 numbers between 1 and 10
print(a) # [ 1.    3.25  5.5   7.75 10.  ] : 5 numbers between 1 and 10

# list to numpy array
a = [1, 2, 3, 4, 5]
b = np.array(a)
print(b) # [1 2 3 4 5] : numpy array

# analysis of numpy array
a = np.array([1, 2, 3, 4, 5])
print(a.shape) # (5,) : 1D array with 5 elements
print(a.size) # 5 : 5 elements
print(a.ndim) # 1 : 1D array
print(a.dtype) # int32 : data type of elements

# reshape numpy array
a = np.array([1, 2, 3, 4, 5, 6])
b = a.reshape(2, 3)
print(b) # [[1 2 3] [4 5 6]] : 2x3 array





