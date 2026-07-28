import numpy as np 

# cube = np.arange(24).reshape(2,3,4)

# print("cube Shape" , cube.shape)
# print ("\nsum of the axis 0" , cube.sum(axis=0).shape )
# print ("\nsum of the axis 1" , cube.sum(axis=1).shape )
# print ("\nsum of the axis 2" , cube.sum(axis=2).shape )
# print("\nsum(axis=(0,1)) ->", cube.sum(axis=(0, 1)).shape, " (collapse two at once)")


marks = np.array([[80, 70, 90],
                  [60, 65, 70],
                  [95, 88, 92],
                  [50, 45, 60]])

# row_means = marks.mean(axis=1)       # shape (4,)
# print("marks shape:    ", marks.shape)
# print("row_means shape:", row_means.shape)

# try:
#     marks - row_means
# except ValueError as e:
#     print("\nValueError:", e)


row_means = marks.mean(axis=1, keepdims=True)     # shape (4, 1) not (4,)
print("with keepdims:", row_means.shape)
print(row_means)

centred = marks - row_means                        # (4,3) - (4,1) -> works
print("\nrow-centred marks:")
print(np.round(centred, 1))
print("\nrow means now:", np.round(centred.mean(axis=1), 10))



grid = np.array([[3, 7, 2],
                 [9, 4, 6]])

flat = grid.argmax()
print("grid.argmax() =", flat, " <- index into the FLATTENED array")

pos = np.unravel_index(flat, grid.shape)
print("unravel_index ->", pos, " (row, col)")
print("value there   :", grid[pos])

# or aggregate along an axis
print("\nargmax(axis=0):", grid.argmax(axis=0), " best row per column")
print("argmax(axis=1):", grid.argmax(axis=1), " best column per row")


import numpy as np

# a real one: the sigmoid function, the classic neural network activation
def sigmoid(x):
    return 1 / (1 + np.exp(-x))

x = np.array([-4, -2, 0, 2, 4], dtype=float)
print("x       :", x)
print("sigmoid :", np.round(sigmoid(x), 4))