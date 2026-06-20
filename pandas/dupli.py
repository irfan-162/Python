import pandas as pd

df = pd.DataFrame({
    'Name': ['A', 'B', 'B', 'C', 'D', 'D'],
    'Marks': [80, 90, 90, 85, 70, 70]
})

#problem 1: find duplicate rows

print(df.duplicated().sum()) # this will give us the count of duplicate rows in the dataframe

#problem 2: drop duplicate rows
df_2 = df.drop_duplicates() # this will drop the duplicate rows from the dataframe and return a new dataframe with unique rows only
print(df_2)

#prob
df_3 = df.drop_duplicates(keep=False) # this will drop all the duplicate rows from the dataframe and return a new dataframe with unique rows only
print(df_3)

if not df_3.empty:
    print(df_3.sum())
    print(len(df_3))  # this will give us the count of rows in the dataframe
else:
    print("No unique rows available.")