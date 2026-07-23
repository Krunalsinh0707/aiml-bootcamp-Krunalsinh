import numpy as np


arr_01 = np.ones((3, 4))
arr_02 = np.array([1, 2, 3, 4])
arr_03 = np.array([1, 2, 3])

fixed_arr_03 = arr_03.reshape(3, 1)
print("arr_01+arr_02", arr_01 + arr_02)  # this runs the code and gives the output
# print("arr_01+arr_03", arr_01+arr_03 )     #this dont work or not run
print("arr_01+fixed_arr_03", arr_01 + fixed_arr_03)


arr_04 = np.ones((3, 1))
arr_05 = np.ones((1, 4))
print(arr_04 + arr_05)


rows = np.arange(1, 11).reshape(-1, 1)  # (10, 1)
cols = np.arange(1, 11)
print(rows)
print(rows * cols)


points = np.array([[1, 2], [3, 4], [5, 6], [7, 8]])

reference = np.array([2, 3])

distance = np.sqrt(np.sum((points - reference) ** 2, axis=1))

print(distance)
