import numbering_practice as np

# 1
# [1,2,3,4]

a = [1, 2, 3]
b = a
b.append(4)
print(a)

# 2
print(0.1 + 0.2 == 0.3)  # false

# 3[1,2,3]
g = (x for x in [1, 2, 3])
print(list(g))
print(list(g))

# 4

A = np.array([[1, 2], [3, 4]])
print(A * A)  # It is normal multiplication
print(A @ A)  # It is matrics multiplication

# 5
m = np.array([[80, 70], [60, 65]])
print(m.mean(axis=0))  # mean column wise

# 6

arr = np.array([1, 2, 3, 4, 5])
s = arr[1:4]
s[0] = 99
print(
    arr
)  # firsr we take part of array 2,3,4,5   now first element is 99 so change the arr

# 7
# float
arr_01 = np.array([1, 2, 3]) / 2

print(arr_01.dtype)

# 8
# error
# sum = np.ones((2,3)) + np.array([1,2])
# print(sum)


# 9

# def f(x, items=[]):   #items should be none

# 10
# ;inespace
print(np.linspace(0, 1, 5))
print(np.arange(0, 1, 0.25))
