import matplotlib.pyplot as plt
import numpy as np

# img = np.random.rand(20, 20)
# plt.imshow(img, cmap='Reds')
# plt.colorbar()
# plt.show()


# img = np.arange(400).reshape(20,20 )
# plt.imshow(img, cmap='grey_r')
# plt.colorbar()
# plt.show()


# 2

gradient = np.linspace(0, 255, 100)

image = np.tile(gradient, (100, 1))

# Display the gradient
plt.imshow(image, cmap="gray", interpolation="nearest")
plt.title("Left-to-Right Gradient")
plt.colorbar()

plt.show()


# 4


board = np.zeros((8, 8))

board[::2, ::2] = 1
board[1::2, 1::2] = 1

print(board)
plt.imshow(board, cmap="gray")

plt.title("Chessboard Pattern")
plt.xticks(range(8), range(1, 9))
plt.yticks(range(8), range(1, 9))

plt.show()


# 5


# Create a 10x10 grayscale image
img = np.arange(100).reshape(10, 10)

# Print shape and data type
print("Shape :", img.shape)
print("Data Type :", img.dtype)

# Slice out the top-left quarter
quarter = img[:5, :5]

# Display the original image
plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray", interpolation="nearest")
plt.title("Original Image")
plt.colorbar()

# Display the quarter image
plt.subplot(1, 2, 2)
plt.imshow(quarter, cmap="gray", interpolation="nearest")
plt.title("Top-Left Quarter")
plt.colorbar()

plt.show()


# 6


# Create a 10x10 grayscale image
img = np.arange(100).reshape(10, 10)

# Flip vertically (top ↔ bottom)
vertical_flip = img[::-1, :]

# Display
plt.figure(figsize=(8, 4))

plt.subplot(1, 2, 1)
plt.imshow(img, cmap="gray", interpolation="nearest")
plt.title("Original")

plt.subplot(1, 2, 2)
plt.imshow(vertical_flip, cmap="gray", interpolation="nearest")
plt.title("Vertical Flip")

plt.show()
