import pandas as pd
s = pd.Series(
    [100, 200, 300],
    index=['X', 'Y', 'Z']
)
s2 = pd.Series([1,2,3])

s2[3] = 4
print(s2) # This will add a new element to the series with index 3 and value 4

s['W'] = 400
s['Y'] = 250

if 'X' in s.index:
    print("X is in the series")
    s.drop('X',inplace=True) # This will remove the element with index 'X' from the series or s = s.drop('X') # This will return a new series without the element with index 'X' but we need to assign it to a new variable or overwrite the existing variable to see the changes
    print(s)

#add multiple data to the series
new_data = pd.Series(
    [88, 95],
    index=['E', 'F']
)

s = pd.concat([s, s2])
print(s) # This will concatenate the two series and return a new series with the combined data
print(s.values) # This will return the values of the series as a numpy array
