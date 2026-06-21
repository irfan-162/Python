import matplotlib.pyplot as plt

marks = [45, 50, 52, 55, 60, 65, 67, 70, 75, 80]

plt.hist(marks, bins=4)
plt.xlabel("Marks")
plt.ylabel("Number of Students")
plt.title("Distribution of Marks")
plt.show()