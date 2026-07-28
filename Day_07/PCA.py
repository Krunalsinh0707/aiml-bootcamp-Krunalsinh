import numpy as np 
import matplotlib.pyplot as plt

rng = np.random.default_rng(42)
f1 = rng.normal(0, 1, 300)
f2 = f1 * 0.9 + rng.normal(0, 0.3, 300) # correlated
f3 = f1 * 0.2 + rng.normal(0, 1.0, 300) 
f4 = rng.normal(0, 1, 300) # independent

X = np.column_stack([f1, f2, f3, f4])

print(X.shape)

mean = X.mean(axis = 0)
std = X.std(axis = 0)

X = X-mean/std

print(X.mean(axis=0))
print(X.std(axis=0))
print (np.allclose(X.mean(axis=0), 0))
print ( np.allclose(X.std(axis=0), 1))

n = X.shape[0]

covariance = (X.T @ X) / (n - 1)

eigenvalues, eigenvectors = np.linalg.eig(covariance)
idx = np.argsort(eigenvalues)[::-1]

eigenvalues = eigenvalues[idx]
eigenvectors = eigenvectors[:, idx]
np.argsort(eigenvalues)
explained_variance = eigenvalues / np.sum(eigenvalues)

principle_component = np.argmax(np.cumsum(explained_variance) >= 0.90) + 1 
X_pca = X @ eigenvectors[:, :2]

compare = np.cov(X.T)
print("eigon Vectors :" ,eigenvectors,"eigonvalurs" , eigenvalues)
print(compare)
print (np.argsort(eigenvalues))
print(explained_variance)
print(principle_component)
# print (covariance)
# print (n)
print (np.allclose(eigenvalues , compare))


plt.scatter(X_pca[:, 0], X_pca[:, 1])
plt.xlabel("Principal Component 1")
plt.ylabel("Principal Component 2")
plt.title("PCA Projection")
plt.show()