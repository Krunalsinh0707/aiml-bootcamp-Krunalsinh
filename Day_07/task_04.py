import numpy as np 
import matplotlib.pyplot as plt

def make_line(n, slope, intercept, noise, seed=0):
    rng = np.random.default_rng(seed)
    x = np.linspace(0, 10, n)
    y = slope * x + intercept + rng.normal(0, noise, n)
    return x, y


noise_levels = [0.5, 2.0, 10.0]

fig, axes = plt.subplots(1, 3, figsize=(15, 5))

for ax, noise in zip(axes, noise_levels):
    x, y = make_line(n=100, slope=2, intercept=5, noise=noise)

    ax.scatter(x, y)
    ax.set_title(f"Noise = {noise}")

plt.tight_layout()
plt.show()

for noise in noise_levels:
    x, y = make_line(n=100, slope=2, intercept=5, noise=noise)

    slope, intercept = np.polyfit(x, y, 1)

    print(f"Noise = {noise}")
    print(f"Recovered slope = {slope:.3f}")
    print()


rng = np.random.default_rng(42)

def make_clusters(n, centres, spread):
        points = []

        for centre in centres:
            cluster = rng.normal(
                loc=centre,
                scale=spread,
                size=(n, 2),
            )
            points.append(cluster)

        return points
overlap = make_clusters(
    n=100,
    centres=[
        [0, 0],
        [2, 2],
    ],
    spread=2,
)

plt.figure(figsize=(6, 6))

colors = ["red", "blue"]

for cluster, color in zip(overlap, colors):
    plt.scatter(cluster[:, 0], cluster[:, 1], c=color)

plt.title("Overlapping Clusters")
plt.show()

separate = make_clusters(
    n=100,
    centres=[
        [0, 0],
        [8, 8],
    ],
    spread=1,
)

plt.figure(figsize=(6, 6))

colors = ["red", "blue"]

for cluster, color in zip(separate, colors):
    plt.scatter(cluster[:, 0], cluster[:, 1], c=color)

plt.title("Separated Clusters")
plt.show()