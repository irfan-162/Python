import numpy as np

arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])

new_arr = np.insert(arr, 1, [10,11,12], axis=0) #insert a new row at index 1
print("Array after insertion:\n", new_arr)
print("Original Array:\n", arr) #original array is unchanged

arr_1D = np.array([1,2,3,4,5])
new_arr_1D = np.insert(arr_1D, 2, [10,11]) #insert 10 and 11 at index 2
print("1D Array after insertion:", new_arr_1D)
print("Original 1D Array:", arr_1D) #original array is unchanged

#append
appended_arr = np.append(arr, [[10,11,12]], axis=0) #append a new row at the end
print("Array after appending:\n", appended_arr)
print("Original Array shape:",arr.shape) #shape of the og array
print("Array shape:",appended_arr.shape) #shape of the new array
print("Original Array:\n", arr) #original array is unchanged

appended_arr_1D = np.append(arr_1D, [10,11]) #append 10 and 11 at the end 
print("1D Array after appending:", appended_arr_1D)
print("Original 1D Array:", arr_1D) #original array is unchanged