import numpy as np

# 1
arr_01 = np.arange(1, 21)

print(arr_01[::-1])

# 2

arr_02 = np.zeros((3, 3))

arr_02[1, 1] = 1

print(arr_02)

# 3

arr_03 = np.arange(20)
print(arr_03[::3])

# 4

arr_04 = np.arange(20)
arr_04[arr_04 % 2 == 1] = -1
mask_a = arr_04 % 2 == 1
arr_04[mask_a] = -1

print(arr_04)

# 5

scores = np.array([45, 88, 32, 91, 67, 40, 78])

mask = scores > scores.mean()

print(scores.mean())
print(scores[mask])

# 6

coun = np.arange(76)
mask = coun >= 25
sum = mask.sum()
print(coun[mask])
print(sum)

# 7
score_01 = np.array([45, 88, 32, 91, 67, 40, 78])

val_01 = np.sort(score_01)[-5:][::-1]

print(val_01)

# 8
arr = np.array([[-1, 2, 0, 4], [4, -0.5, 6, 0], [2.6, 0, 7, 8], [3, -7, 4, 2.0]])

arr[[0, 3]] = arr[[3, 0]]

print(arr)

# 9
grid = np.arange(1, 17).reshape(4, 4)

print(grid)

# 10
print(grid[:, 1], grid[-2:])

# 11
print(grid.sum(axis=0))  # Gives sum of each column
print(grid.sum(axis=1))  # gives sum of each row

# 12

normalized = (grid - grid.mean(axis=0)) / grid.std(axis=0)

print(normalized)
print(normalized.mean())
print(normalized.std())

# 13

one = np.ones((5, 5))
zero = np.zeros((3, 3))
one[1:4, 1:4] = zero
print(one)

# 14

print(arr.argmax())
print(np.unravel_index(arr.argmax(), arr.shape))


# 15

arr1 = np.array([45, 41, 12])
arr2 = np.array([54, 14, 21])

rowsp = np.vstack((arr1, arr2))
columnsp = np.column_stack((arr1, arr2))

print(rowsp)
print(columnsp)
