import pandas as pd

# Create a basic NumPy array (series)
data = pd.Series([10, 20, 30, 40, 50],name="Numbers")

print("Original Series:",data)
print("Greater than 10 numbers:",data[data > 10])
data.name = "Num2"
data.index = ['a', 'b', 'c', 'd', 'e']
print(data)
data.loc['a'] = 100
print(data['a']) #data[0] throw error cause it will try to find index 0 which is not exist but data.loc['a'] will work because it will try to find index 'a' which exist

#iloc is used to access the data by position eg data.iloc[0] will return the first element of the series which is 100

data.iloc[0] = 200
print(data) #data.iloc[0] will return the first element of the series which is 200