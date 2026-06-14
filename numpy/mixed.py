import numpy as np
#prob1
X = np.random.randint(0,100,size=(10,4))
print("Column Mean:\n", np.mean(X, axis=0))
print("Column standard deviation:\n", np.std(X, axis=0))

#prob2
arr = np.random.randint(1, 100,size=(100,3))
print(arr.shape)
weight = np.random.randn(3, 1)
print(weight.shape)
y = arr @ weight
print("Output shape:", y.shape)
print(y)

X = np.random.randint(1,50,(5,4))
print(np.max(X, axis=1)) #max of each row