import pandas as pd
df = pd.DataFrame({
      'A': [1, 2, 3, 4, 5],
      'B': ['a', 'b', 'c', 'd', 'e'],
      'C': [10.5, 20.3, 30.1, 40.2, 50.0]
      },index=['row1', 'row2', 'row3', 'row4', 'row5'])
print(df)
print(df['A']) #accessing column A
print(df.loc['row3']) #accessing row with label 'row3'
print(df.iloc[2]) #accessing row with integer index 2
print(df.loc['row2', 'B']) #accessing specific value at row 'row2' and column 'B'
print(df[df['A'] > 2]) #filtering rows where column A is greater than 2
print(df.iloc[:,:-1])
