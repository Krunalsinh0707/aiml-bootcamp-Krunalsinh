import matplotlib.pyplot as plt
import timeit

sizes = [1_000, 10_000, 100_000, 1_000_000]
speedup_squere = []
speedup_sum = []
speedup_dot = []

for n in sizes:
    setup = f"import numpy as np; lst = list(range({n})); arr = np.arange({n})"
    py_sq = timeit.timeit("[x * 2 for x in lst]", setup=setup, number=20) / 20
    np_sq = timeit.timeit("arr * 2", setup=setup, number=20) / 20
    speedup_squere.append(py_sq / np_sq)
    print(
        f"For Squere , n = {n:>9,}   python {py_sq*1000:7.2f} ms   numpy {np_sq*1000:6.3f} ms   {py_sq/np_sq:5.0f}x"
    )


for n in [1_000, 10_000, 100_000, 1_000_000]:
    setup = f"import numpy as np; lst = list(range({n})); arr = np.arange({n})"

    pyt = (
        timeit.timeit(
            """
total = 0
for x in lst:
    total += x
""",
            setup=setup,
            number=20,
        )
        / 20
    )

    npt = timeit.timeit("arr.sum()", setup=setup, number=20) / 20

    speedup_sum.append(pyt / npt)

    print(
        f"For Sum , n = {n:>9,}   python {pyt*1000:7.2f} ms   numpy {npt*1000:6.3f} ms   {pyt/npt:5.0f}x"
    )


for n in [1_000, 10_000, 100_000, 1_000_000]:
    setup = f"""
import numpy as np
lst1 = list(range({n}))
lst2 = list(range({n}))
arr1 = np.arange({n})
arr2 = np.arange({n})
"""

    pyd = (
        timeit.timeit(
            """
dot = 0
for a, b in zip(lst1, lst2):
    dot += a * b
""",
            setup=setup,
            number=20,
        )
        / 20
    )

    npd = timeit.timeit("np.dot(arr1, arr2)", setup=setup, number=20) / 20

    speedup_dot.append(pyd / npd)
    print(
        f"for Dot , n = {n:>9,}   python {pyd*1000:7.2f} ms   numpy {npd*1000:6.3f} ms   {pyd/npd:5.0f}x"
    )

plt.plot(sizes, speedup_squere, marker="o", label="Square")
plt.plot(sizes, speedup_sum, marker="s", label="Sum")
plt.plot(sizes, speedup_dot, marker="^", label="Dot Product")

plt.title("NumPy Speedup vs Array Size")
plt.xlabel("Array Size")
plt.ylabel("Speedup (Python / NumPy)")
plt.xticks(sizes, ["1K", "10K", "100K", "1M"])
plt.grid(True)
plt.legend()

plt.show()
