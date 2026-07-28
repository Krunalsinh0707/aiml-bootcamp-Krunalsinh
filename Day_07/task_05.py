import numpy as np 


print(0.1 + 0.2 != 0.3)
print(repr(0.1 + 0.2))
print(0.45 + 0.84 == 1.29)    #it gives true value 
print(0.4 + 0.8 == 1.2)       # it gives false value boolean

small = np.array([1, 2, 3], dtype=np.int8)
print(small * 100)

x = np.float32(1e8)
print(np.float32(x + 1) - x)

a = np.float32(100000000.1)
b = np.float32(100000000.0)
print("a - b =", a - b)     #shuould be 0.1

n = 1_000_000

arr32 = np.full(n, 0.1, dtype=np.float32)
arr64 = np.full(n, 0.1, dtype=np.float64)

sum32 = arr32.sum(dtype=np.float32)
sum64 = arr64.sum(dtype=np.float64)

exact = n * 0.1


print(sum32)
print(sum64)
print(exact)

#use float64
