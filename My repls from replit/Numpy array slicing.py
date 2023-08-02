"""
Slicing (lesson summary)

[<row> START : STOP : STEP,  <column> START : STOP : STEP]

NumPy example:
"""

import numpy as np 

a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
arr = np.array(a)

print(a) # -> [1,2,3,4,5,6,7,8,9] 
print(arr) # ->[1 2 3 4 5 6 7 8 9]

# Slicing... 
print(arr[: :2]) # ->[1 3 5 7 9]
print(arr[2: :]) # ->[3 4 5 6 7 8 9]
print(arr[:2:]) # ->[1 2]
print(arr[2:2:]) # ->[ ]
print(arr[2:2:2]) # ->[ ] 
print(arr[:2:2]) # -> [1]

# array indexing is same as list indexing

arr1 = np.array([1,2,3,4,5])
print(arr1[0])
#>> 1

# for 2 dimentional arrays
arr2 = np.array([[1,2,3], [4,5,6]])
print(arr2[1][0])  # array[row][column]
#>> 4
print(arr2[1,0])   ## array[row, column]
#>> 4

#slicing
arr1 = np.array([1,2,3,4,5])
print(arr1[1:3])
#>> [2 3]

# for 2 dimentional arrays
arr2 = np.array([[1,2,3], [4,5,6]])
print(arr2[0,:])  # row index zero and all columns
#>>  [1, 2, 3]
print(arr2[0,0:2])  # row index zero and first 2 columns
#>> [1 2]
print(arr2[:,1])  # all rows and only column index 1
#>> [2 5]

      
