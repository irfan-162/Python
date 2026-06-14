import numpy as np
X = np.random.randint(1,50,(5,4))
mean = np.mean(X, axis=0)
print("Mean of each column:\n", mean)
std = np.std(X, axis=0)
norm = (X - mean)/std
print("mean", np.mean(norm, axis=0))
print("std", np.std(norm, axis=0))
