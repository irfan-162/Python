import numpy as np
arr1 = np.array([[1,2,3],
                  [4,5,6],
                  [7,8,9]])
arr1_1D = np.array([1,2,3,4,5])
arr2_1D = np.array([10,11,12,13,14])
#stack
stacked_arr = np.stack((arr1, arr1), axis=0) #stack arr1 on top of itself along a new axis
print("Stacked Array:\n", stacked_arr)
print(stacked_arr.ndim) #number of dimensions of the stacked array

st2 = np.vstack((arr1_1D, arr2_1D)) #stack arr1_1D and arr2_1D along a new axis
print("Stacked 1D Array:\n", st2)
print(st2.ndim) #number of dimensions of the stacked 1D array

st3 = np.hstack((arr1_1D, arr2_1D)) #stack arr1 and arr1 horizontally (column-wise)
print("Horizontally Stacked Array:\n", st3)
print(st3.ndim) #number of dimensions of the horizontally stacked array

#split
split_arr = np.split(arr1, 3) #split arr1 into 3 equal parts along the first axis + returns a "list" not array of 3 arrays
print("Split Array:\n", split_arr)
