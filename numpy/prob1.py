import numpy as np
arr1 = np.array([[1,2,3,5,6],
                  [4,5,6,6,7],
                  [7,8,9,8,1]])
print(np.sum(arr1, axis=1)) #sum of each column
print(arr1[0:2, 3:5]) #slicing the array to get the first two rows and last two columns
print(arr1[1]) #slicing the array to get the second row
print("sub1:",arr1[0:2, 1]) #slicing the array to get the first two rows and second column
print(arr1[:, 1]) #slicing the array to get all rows and second column
print(arr1[1,0])
print(arr1[::-1, ::-1])
print(np.sum(arr1, axis=0)) #sum of each row
print(np.dot(arr1, arr1.T)) #dot product of the array with its transpose