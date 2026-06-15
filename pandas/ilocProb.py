import pandas as pd
import numpy as np

df = pd.DataFrame({
    'Age': [20, 25, 30, np.nan, 28, 22],
    'Salary': [30000, 50000, 70000, 60000, np.nan, 35000],
    'Experience': [1, 3, 5, 4, 2, 1],
    'Department': ['IT', 'HR', 'IT', 'Sales', 'HR', 'IT'],
    'Target': [0, 1, 1, 0, 1, 0]
})

#prob1
print("Problem 1: Display the first 3 rows of the DataFrame",df.head(3))
print("Problem 1: Display the last 2 rows of the DataFrame",df.tail(2))

#prob2
print("Problem 2: Display the shape of the DataFrame",df.shape)
print("Problem 2: Display the column names of the DataFrame",df.columns)
print("Problem 2: Display the data types of each column in the DataFrame",df.dtypes)

#prob3
print(df[['Age', 'Salary']]) #displaying specific columns

#prob4
print(df.iloc[:,:3]) #displaying specific row using integer index

#prob5
print(df[df['Age'] > 25]) #filtering rows based on condition])
print(df[df['Department'] == 'IT']) #filtering rows based on condition
print(
    df[
        (df['Department'] == 'IT') &
        (df['Salary'] > 40000)
    ]
)

print(
    df[
        (df['Department'] == 'HR') |
        (df['Age'] < 30)
    ]
)

#prob6

df = pd.DataFrame({
    "Name": ["Alice", "Bob", "Charlie", "David", "Eva"],
    "Age": [20, 25, 30, 22, 28],
    "CGPA": [3.5, 3.8, 3.2, 3.9, 3.7],
    "Placed": [0, 1, 0, 1, 1]
}, index=[101, 102, 103, 104, 105])

print("cgpa of the student with label 104: ",df.loc[104,'CGPA']) 
print("3rd row of placed column: ",df.iloc[2,3])

#prob7

import pandas as pd

df = pd.DataFrame({
    "Hours_Study": [2, 5, 1, 7, 4],
    "Attendance": [70, 90, 60, 95, 80],
    "Assignments": [5, 9, 4, 10, 8],
    "Pass": [0, 1, 0, 1, 1]
})

X = df.iloc[:, :-1]
y = df.iloc[:, -1]
print(X.shape) #output should be (5, 3)
print(X.ndim) #output should be 2
print(y.shape) #output should be (5,)
print(y.ndim) #output should be 1