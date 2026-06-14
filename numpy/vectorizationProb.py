import numpy as np
#prob1
x = np.array([1,2,3,4,5])
print(3*x**2 + 2*x + 1) #vectorized operation on the array

#prob2
arr = np.array([10,20,30,40,50])
print((arr > 25).astype(int)) #vectorized comparison and type conversion

#prob3
y = np.arange(1,1000001)
print(y)
X = np.random.rand(100, 5) #100 samples, 5 features
W = np.random.rand(5, 1) #5 features, 1 output
X.shape = (100, 5)
W.shape = (5, 1)
print((X @ W).shape) #matrix multiplication using vectorization