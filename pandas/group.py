import pandas as pd

df = pd.DataFrame({
    'Department': ['IT', 'HR', 'IT', 'HR', 'Sales'],
    'Salary': [50000, 40000, 60000, 45000, 55000],
    "Experience": [2,1,5,4,3]
})

print(df.groupby('Department').size()) # this will give us the count of rows in each group based on the 'Department' column

print(df.groupby('Department')['Salary']
      .agg(['mean','max','min']))

print(df.groupby('Department')[['Salary','Experience']].agg(['mean','max','min'])) # this will give us the mean, max and min of the 'Salary' and 'Experience' columns for each group based on the 'Department' column


avg_salary = df.groupby('Department')['Salary'].mean()

print(avg_salary)

print("\nDepartment with highest average salary:")
print(avg_salary.idxmax())