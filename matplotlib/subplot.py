import matplotlib.pyplot as plt

# plt.subplot(1,2,1)
# plt.plot([1,2,3],[4,5,6])
# plt.title("Line")

# plt.subplot(1,2,2)
# plt.bar(["A","B","C"], [5,7,4])
# plt.title("Bar")

# plt.show()

plt.subplot(2, 2, 1)
plt.plot([1, 2, 3], [1, 4, 9])

plt.subplot(2, 2, 2)
plt.scatter([1, 2, 3], [1, 4, 9])

plt.subplot(2, 2, 3)
plt.bar(['A', 'B', 'C'], [3, 5, 2])

plt.subplot(2, 2, 4)
plt.hist([1, 2, 2, 3, 3, 3, 4])

plt.show()