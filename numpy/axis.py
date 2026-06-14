import numpy as np
#prob1
X = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])
print("sum of each row",np.sum(X, axis=1)) #sum of each row
print("sum of each column",np.sum(X, axis=0)) #sum of each column
print("mean of each column",np.mean(X, axis=0)) #mean of each column
print("mean of each row",np.mean(X, axis=1)) #mean of each row
print(np.max(X, axis=1)) #max of each row

#prob2
marks = np.array([
    [80,90,70],
    [60,75,85],
    [90,88,92]
])
print("average marks of each student",np.mean(marks, axis=1).astype(int)) #average marks of each student
print("average marks of each subject",np.mean(marks, axis=0).astype(int)) #average marks of each subject