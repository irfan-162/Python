import matplotlib.pyplot as plt
subjects = ["Math", "Physics", "Chemistry"]
marks = [85, 90, 80]

plt.bar(subjects, marks)

plt.xlabel("Subject")
plt.ylabel("Marks")
plt.title("Subject Marks")

plt.show()