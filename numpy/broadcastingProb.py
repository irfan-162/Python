import numpy as np
#prob1
X = np.array([
    [10, 100],
    [20, 200],
    [30, 300]
])
mean = np.mean(X, axis=0)
print("Mean:", mean)
ans = X - mean
print("Broadcasted Subtraction:\n", ans)

#prob2
X2 = np.array([
    [1,2,3],
    [4,5,6],
    [7,8,9]
])

v = np.array([10,20,30])
broadcasted_sum = X2 + v
print("Broadcasted Addition:\n", broadcasted_sum)

#prob3
X = np.array([
    [1],
    [2],
    [3]
])

v = np.array([10,20,30])
broadcasted_sum = X + v #should be 3 X 3
print("Shape is :\n", broadcasted_sum.shape)