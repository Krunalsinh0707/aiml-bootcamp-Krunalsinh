import numpy as np 
import timeit

A = np.array([[2., 3., -1.],
             [4., -1., 2.],
             [-1., 2., 3.]])
b = np.array([5., 6., 7.])


x = np.linalg.solve(A,b)
print (x)
print(np.allclose(A @ x, b)) #uses np.allclose because float numbering

y = (np.linalg.inv(A) @ b)
print (y)

print(np.allclose(x , y) )




setup = "import numpy as np; A = np.random.rand(500, 500); b = np.random.rand(500)"

t_solve = timeit.timeit("np.linalg.solve(A, b)", setup=setup, number=20) / 20
t_inv = timeit.timeit("np.linalg.inv(A) @ b", setup=setup, number=20) / 20

print(f"np.linalg.solve(A, b): {t_solve*1000:6.2f} ms")
print(f"np.linalg.inv(A) @ b : {t_inv*1000:6.2f} ms")
print(f"\nsolve is about {t_inv/t_solve:.1f}x faster")


singular = np.array([[1., 2.],
                     [2., 4.]])      # row 2 = 2 x row 1

print("determinant:", np.linalg.det(singular))

try:
    np.linalg.inv(singular)
except np.linalg.LinAlgError as e:
    print("LinAlgError:", e)


    #solve preffer above inv because it takes less time than inv 
    #det it means as the the matrix given is a singular matrix
    # linear dependence 
     