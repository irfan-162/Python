import pandas as pd
import numpy as np

#prob1
df = pd.DataFrame({
    "Age": [20, np.nan, 30, np.nan, 25],
    "Salary": [30000, 50000, np.nan, 45000, np.nan],
    "Experience": [1, 3, np.nan, 2, 5]
})

df_clean1 = df.dropna(how='any')
print(len(df_clean1))

#prob2
df_clean2 = df.fillna(0)
print(df_clean2)

#prob3
mean_age = df['Age'].mean()
df_clean3 = df['Age'].fillna(mean_age)
print('prob3 : ',df_clean3)

#prob4
median_sal = df['Salary'].median()
df_clean4 = df['Salary'].fillna(median_sal)
print('prob4 : ',df_clean4)

#prob5
mean_exp = df['Experience'].mean()
df['Age'] = df['Age'].fillna(mean_age)
df['Salary'] = df['Salary'].fillna(median_sal)
df['Experience']  = df['Experience'].fillna(mean_exp)

X = df.iloc[:,:]
print(X)

