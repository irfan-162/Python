import numpy as np
#prob1
arr = np.arange(1,25) #creating an array of 24 elements
print(arr.shape) #shape of the array
print(arr.reshape(2,12))
print(arr.reshape(4,6))
print(arr.reshape(3,8))
#prob2
b = np.arange(60)
print(b.reshape(5,12))

#prob3
images = np.arange(200)
print(images.shape) #shape of the array
print("Total Images:", int(200/25))
print("Final Arrangement:", images.reshape(8,5,5).ndim)