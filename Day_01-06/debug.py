import numpy as np


def add(score, marks=[]):
    marks.append(score)
    return marks


print(add(10))
print(add(20))


total = 0.1 + 0.2


# if total == 0.3:
#     print("Equal")
# else:
#     raise ValueError("Values are not equal")


def numbers():
    for i in range(5):
        yield i


gen = numbers()

print(list(gen))


a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6], [7, 8]])

print(a * b)

print(a @ b)
