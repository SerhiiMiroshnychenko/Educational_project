import numpy as np

# array[row, column]
# remember indexing starts from zero.

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

nums_arr = np.array(nums)
nums_arr[3] = 33
print(nums_arr)

tens = [10, 10, 20, 30, 40, 50, 60, 70, 80, 90]

nums_and_tens = nums + tens
nums_and_tens_arr = np.array(nums_and_tens)
nums_and_tens_arr = nums_and_tens_arr.reshape((2,10))
print(nums_and_tens_arr)
nums_and_tens_arr[0, 3] = 333
print(nums_and_tens_arr[1, 4])
nums_and_tens_arr[1, 4] = 444
print(nums_and_tens_arr)

nums_and_tens_arr[0,:] = 14
print(nums_and_tens_arr)

nums_and_tens_arr[:5, :5] = 0
print(nums_and_tens_arr)

nums_and_tens_arr = nums_and_tens_arr.reshape((2,2,5))

print('\nNew arr: ', nums_and_tens_arr)

print(nums_and_tens_arr.shape)


nums_and_tens_arr[:,:, 0] = [[111, 222], [333, 444]]
print('\nArr55: ', nums_and_tens_arr)

nums_and_tens_arr[:, :, :2] = 777
print('', )
