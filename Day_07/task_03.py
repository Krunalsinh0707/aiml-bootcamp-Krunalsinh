import numpy as np

a = np.array([1, 2])
b = np.array([1, 2])


def cosine_similarity(a, b):
    return (a @ b) / (np.linalg.norm(a) * np.linalg.norm(b))


print(cosine_similarity(a, b))

print(np.isclose(cosine_similarity(a, b), 1))

a = np.array([1, 2])
b = np.array([-1, -2])


print(cosine_similarity(a, b))

print(np.isclose(cosine_similarity(a, b), -1))

a = np.array([1, 0])
b = np.array([0, 1])


print(cosine_similarity(a, b))

print(np.isclose(cosine_similarity(a, b), 0))


rng = np.random.default_rng(42)
vectors = rng.random((100, 50))
query = rng.random(50)

dot_product = vectors @ query

vector_norms = np.linalg.norm(vectors, axis=1)

query_norms = np.linalg.norm(query)

similarities = dot_product / (vector_norms * query_norms)

print(similarities)
print(similarities.shape)

vectors_new = rng.random((100, 100))

normalized_vectors = vectors_new / np.linalg.norm(vectors, axis=1, keepdims=True)

similarity_matrix = normalized_vectors @ normalized_vectors

print(similarity_matrix)
print(similarity_matrix.shape)
