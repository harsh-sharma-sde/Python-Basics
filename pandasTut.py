# pandas module python tutorial

import pandas as pd

# pandas is a data manipulation library that provides data structures like series and dataframes to manipulate data.

# Series
# A series is a one-dimensional array that can hold any data type such as integers, floats, and strings.
# A series can be created using various inputs like:
# - Array
# - Dict
# - Scalar value or constant

# Creating a series from an array
data = [1, 2, 3, 4, 5]
series = pd.Series(data)
print(series) # Output: 0    1

# Creating a series from a dictionary
data = {'a': 0, 'b': 1, 'c': 2}
series = pd.Series(data)
print(series) # Output: a    0

# Creating a series from a scalar value
data = 5
series = pd.Series(data)
print(series) # Output: 0    5

# DataFrames
# A DataFrame is a two-dimensional data structure that can hold columns of different data types.
# A DataFrame can be created using various inputs like:
# - Lists
# - Dict
# - Series
# - Numpy arrays
# - Another DataFrame

# Creating a DataFrame from a list
data = [1, 2, 3, 4, 5]
df = pd.DataFrame(data)
print(df) # Output: 0    1

# Creating a DataFrame from a dictionary
data = {'Name': ['Tom', 'Jerry'], 'Age': [20, 21]}
df = pd.DataFrame(data)
print(df) # Output: Name    Age

# Creating a DataFrame from a series
data = pd.Series([1, 2, 3, 4, 5])
df = pd.DataFrame(data)
print(df) # Output: 0    1

# Creating a DataFrame from a numpy array
import numpy as np
data = np.array([[1, 2, 3], [4, 5, 6]])
df = pd.DataFrame(data)

# Creating a DataFrame from another DataFrame
data = {'Name': ['Tom', 'Jerry'], 'Age': [20, 21]}
df = pd.DataFrame(data)
df2 = pd.DataFrame(df)
print(df2) # Output: Name    Age

# Reading and Writing Data
# Pandas can read data from various file formats like CSV, Excel, JSON, etc.
# It can also write data to these formats.

# Reading data from a CSV file
data = pd.read_csv('data.csv')
print(data)

# Writing data to a CSV file
data.to_csv('data.csv')

# Reading data from an Excel file
data = pd.read_excel('data.xlsx')
print(data) # Output: Name    Age

# Writing data to an Excel file
data.to_excel('data.xlsx')

# Reading data from a JSON file
data = pd.read_json('data.json')
print(data)

# Writing data to a JSON file
data.to_json('data.json')

# Indexing and Selecting Data
# Pandas provides various methods to index and select data from a DataFrame.

# Selecting a column
data = {'Name': ['Tom', 'Jerry'], 'Age': [20, 21]}
df = pd.DataFrame(data)

print(df['Name']) # Output: 0    Tom

# Selecting multiple columns
print(df[['Name', 'Age']]) # Output: Name    Age

# Selecting rows
print(df.loc[0]) # Output: Name    Tom

# Selecting multiple rows
print(df.loc[[0, 1]]) # Output: Name    Age

# Selecting rows and columns
print(df.loc[0, 'Name']) # Output: Tom

# Filtering Data
# Pandas provides various methods to filter data from a DataFrame.

# Filtering data based on a condition
data = {'Name': ['Tom', 'Jerry'], 'Age': [20, 21]}
df = pd.DataFrame(data)

print(df[df['Age'] > 20]) # Output: Name    Age

# Filtering data based on multiple conditions
print(df[(df['Age'] > 20) & (df['Name'] == 'Jerry')]) # Output: Name    Age

# Sorting Data
# Pandas provides various methods to sort data in a DataFrame.

# Sorting data by a column
data = {'Name': ['Tom', 'Jerry'], 'Age': [20, 21]}
df = pd.DataFrame(data)

print(df.sort_values('Age')) # Output: Name    Age

# Sorting data in descending order
print(df.sort_values('Age', ascending=False)) # Output: Name

# Grouping Data
# Pandas provides various methods to group data in a DataFrame.

# Grouping data by a column
data = {'Name': ['Tom', 'Jerry', 'Tom', 'Jerry'], 'Age': [20, 21, 20, 21]}
df = pd.DataFrame(data)

print(df.groupby('Name').sum()) # Output: Age

# Grouping data by multiple columns
print(df.groupby(['Name', 'Age']).sum()) # Output: Age

# Merging Data
# Pandas provides various methods to merge data from multiple DataFrames.

# Merging data by a column
data1 = {'Name': ['Tom', 'Jerry'], 'Age': [20, 21]}
data2 = {'Name': ['Tom', 'Jerry'], 'Age': [20, 21]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print(pd.merge(df1, df2, on='Name')) # Output: Name    Age

# Merging data by multiple columns
print(pd.merge(df1, df2, on=['Name', 'Age'])) # Output: Name    Age

# Concatenating Data
# Pandas provides various methods to concatenate data from multiple DataFrames.

# Concatenating data by rows
data1 = {'Name': ['Tom', 'Jerry'], 'Age': [20, 21]}
data2 = {'Name': ['Tom', 'Jerry'], 'Age': [20, 21]}
df1 = pd.DataFrame(data1)
df2 = pd.DataFrame(data2)

print(pd.concat([df1, df2])) # Output: Name    Age

# Concatenating data by columns
print(pd.concat([df1, df2], axis=1)) # Output: Name    Age

# Reshaping Data
# Pandas provides various methods to reshape data in a DataFrame.

# Pivoting data
data = {'Name': ['Tom', 'Jerry'], 'Age': [20, 21]}
df = pd.DataFrame(data)

print(df.pivot(index='Name', columns='Age')) # Output: Name    Age

# Melting data
data = {'Name': ['Tom', 'Jerry'], 'Age': [20, 21]}
df = pd.DataFrame(data)

print(pd.melt(df)) # Output: variable    value

# Handling Missing Data
# Pandas provides various methods to handle missing data in a DataFrame.

# Dropping missing data
data = {'Name': ['Tom', 'Jerry', None], 'Age': [20, 21, None]}
df = pd.DataFrame(data)

print(df.dropna()) # Output: Name    Age

# Filling missing data
print(df.fillna(0)) # Output: Name    Age

# Replacing missing data
print(df.replace({None: 'Unknown'})) # Output: Name    Age

# Handling Duplicates
# Pandas provides various methods to handle duplicates in a DataFrame.

# Dropping duplicates
data = {'Name': ['Tom', 'Jerry', 'Tom'], 'Age': [20, 21, 20]}
df = pd.DataFrame(data)

print(df.drop_duplicates()) # Output: Name    Age

# Counting duplicates
print(df.duplicated().sum()) # Output: 1

# Handling Outliers
# Pandas provides various methods to handle outliers in a DataFrame.

# Detecting outliers
data = {'Name': ['Tom', 'Jerry', 'Tom'], 'Age': [20, 21, 100]}
df = pd.DataFrame(data)

print(df[(df['Age'] - df['Age'].mean()).abs() > 2 * df['Age'].std()]) # Output: Name    Age

# Removing outliers
df = df[(df['Age'] - df['Age'].mean()).abs() <= 2 * df['Age'].std()]

# Handling Categorical Data
# Pandas provides various methods to handle categorical data in a DataFrame.

# Encoding categorical data
data = {'Name': ['Tom', 'Jerry', 'Tom'], 'Age': [20, 21, 20]}
df = pd.DataFrame(data)

print(pd.get_dummies(df)) # Output: Age    Name

# Encoding ordinal data
data = {'Name': ['Tom', 'Jerry', 'Tom'], 'Age': [20, 21, 20]}
df = pd.DataFrame(data)

print(df['Name'].astype('category').cat.codes) # Output: 0    1

# Handling Time Series Data
# Pandas provides various methods to handle time series data in a DataFrame.

# Converting data to datetime
data = {'Date': ['2022-01-01', '2022-01-02', '2022-01-03'], 'Value': [1, 2, 3]}
df = pd.DataFrame(data)

df['Date'] = pd.to_datetime(df['Date'])

# Extracting date components
df['Year'] = df['Date'].dt.year
df['Month'] = df['Date'].dt.month
df['Day'] = df['Date'].dt.day

# Calculating time differences
df['Difference'] = df['Date'].diff()

# Handling Text Data
# Pandas provides various methods to handle text data in a DataFrame.

# Splitting text data
data = {'Name': ['Tom Jerry', 'Jerry Tom']}
df = pd.DataFrame(data)

print(df['Name'].str.split(' ')) # Output: 0    [Tom, Jerry]

# Extracting text data
print(df['Name'].str.extract(r'(\w+) (\w+)')) # Output: 0    1

# Replacing text data
print(df['Name'].str.replace('Tom', 'Jerry')) # Output: 0    Jerry Jerry

# Handling Numerical Data
# Pandas provides various methods to handle numerical data in a DataFrame.

# Scaling numerical data
data = {'Value': [1, 2, 3]}
df = pd.DataFrame(data)

print((df['Value'] - df['Value'].mean()) / df['Value'].std()) # Output: 0   -1

# Normalizing numerical data
print((df['Value'] - df['Value'].min()) / (df['Value'].max() - df['Value'].min())) # Output: 0    0


