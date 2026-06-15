import numpy as np
array_2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print("Original 2D Array:\n", array_2d)
print(array_2d[:, :-1]) # This will return all rows and all columns except the last one
print(array_2d[:, -1]) # This will return all rows and only the last column, it will return a 1D array because we are only selecting one column