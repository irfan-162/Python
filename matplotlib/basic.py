import matplotlib.pyplot as plt
import pandas as pd

x = [1,2,3]
y = [2,7,9]

# plt.plot(x,y)
# plt.grid()
# plt.show()

# df = pd.DataFrame({
#     'Salary': [50000, 60000, 55000, 80000, 75000]})
# plt.xlabel('Employee')
# plt.ylabel('Salary')
# plt.title('Employee Salary')
# plt.plot(df['Salary'],marker='o',linestyle=':',color='r')
# plt.show()

#double plot
# x = [1,2,3,4]

# y1 = [10,20,15,25]
# y2 = [8,12,18,30]

# plt.plot(x, y1)
# plt.plot(x, y2)

# plt.show()

#legend

# x = [1,2,3,4]

# y1 = [10,20,15,25]
# y2 = [8,12,18,30]

# plt.plot(x, y1, label="Product A")
# plt.plot(x, y2, label="Product B")

# plt.legend()

# plt.show()

#problem1
x = [1,2,3,4,5]
y = [3,7,5,10,8]

plt.title('Performance')
plt.xlabel('Day')
plt.ylabel('Score')
plt.plot(x, y, marker='o', linestyle='--', color='g')
plt.grid()
plt.show()

#problem2

months = [1,2,3,4]

income = [50,60,70,90]
expense = [40,55,65,75]

plt.plot(months, income, label='Income', marker='o', color='b')
plt.plot(months, expense, label='Expense', marker='s', color='r',linestyle='--')

plt.show()
