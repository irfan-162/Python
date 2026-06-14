import numpy as np

arr1 = np.array([[1,2,3]])
arr2 = np.array([[11,22,33]])
print("Array 1 dim:\n", arr1.ndim)
new_arr = np.concatenate((arr1, arr2),axis=0) #concatenate arr1 and arr2
print(new_arr)

