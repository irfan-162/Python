import numpy as np

arr = np.array([[1,2,3],
                [4,5,6],
                [7,8,9]])
print("Array:", arr ** 2) #power of 2
print("Max:", np.max(arr)) #max func---agg func
print("STD:", np.std(arr)) #standard deviation

print("at index 0,0 :",arr[0,0])
arr[0,0] = 100
print("Array after change:", arr)

rarr = arr.reshape(1,9) #reshape to 1 row and 9 columns
print("Reshaped Array:", rarr)
print("Original Array:", arr) #original array is unchanged


#flat&ravel
flat = arr.flatten() #flatten the array to 1D
print("Flattened Array:", flat)
flat[0] =999
print("original :",arr)

rav = arr.ravel() #flatten the array to 1D
rav[0]  = 999
print("Raveled Array:", rav)
print("Original Array after ravel change:", arr) #original array is changed