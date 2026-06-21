import numpy as np
import matplotlib.pyplot as plt

np.random.seed(0)

hours = np.random.randint(1, 10, 50)
marks = hours*8 + np.random.randint(-10, 10, 50)

plt.subplot(1,2,1)
plt.scatter(hours, marks)
plt.grid()
plt.xlabel("Hours Studied")
plt.ylabel("Marks Obtained")
plt.title("Hours Studied vs Marks Obtained")

plt.subplot(1,2,2)
plt.hist(marks, bins=8)
plt.grid()
plt.xlabel("Marks Obtained")
plt.ylabel("Number of Students")
plt.title("Distribution of Marks")

plt.show()