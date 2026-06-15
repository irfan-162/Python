import pandas as pd
s = pd.Series(
    [85, 90, 78, 92, 88],
    index=['A', 'B', 'C', 'D', 'E']
)
print("Original Series:", s)
print("Accessing element at C:", s.loc['C'])  # Accessing element by label
print("Accessing element at C:",s['C']) # Accessing element by label using indexing operator
print("Accessing element at position 3:", s.iloc[3])  # Accessing element by position
print("B to D",s.loc['B':'D']) # Accessing a range of elements by label
print(s[s > 85]) # Accessing elements based on a condition
print(int(s.mean())) # Accessing the mean of the series