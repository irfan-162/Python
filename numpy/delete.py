import numpy as np

arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
arr_1D = np.array([1,2,3,4,5])

print(np.delete(arr_1D, 1)) #delete the row at index 1

print(np.delete(arr, 0, axis=0)) #delete the row at index 0 ,,original array remain unchanged
print(f"After deleteing column 1 :{np.delete(arr, 1, axis=1)}") #delete the column at index 1 ,,original array remain unchanged