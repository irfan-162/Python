import pandas as pd

df = pd.DataFrame({
    "Age": [20, 25, 30, 22, 28],
    "Department": ["IT", "HR", "Sales", "IT", "HR"],
    "Education": ["BSc", "MSc", "BSc", "PhD", "MSc"],
    "Target": [0, 1, 1, 0, 1]
})

df_encoded01 = pd.get_dummies(df, columns=["Department"], drop_first=True,dtype=int)  # drop_first=True to avoid dummy variable trap
print(df_encoded01)

df_encoded02 = pd.get_dummies(df, columns=['Department', 'Education'], drop_first=True, dtype=int)
print(df_encoded02)

X = df_encoded02.iloc[:, :-1]  # all columns except the last one (Target)
X_numpy = X.to_numpy()  # convert the DataFrame to a NumPy array
print(X_numpy)