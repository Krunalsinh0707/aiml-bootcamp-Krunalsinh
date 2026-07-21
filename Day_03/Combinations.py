from itertools import combinations, permutations, product, chain

students = ["Krunal", "Rahul", "Asha", "Meera", "Ravi"]

pairs = list(combinations(students, 2))
print(len(pairs))
print(pairs)

per_pairs = list(permutations(students, 2))
print(len(per_pairs))
print(per_pairs)


shirt_color = ["white", "black", "maroon"]
shirt_size = ["M", "XL"]

shirt_pairs = list(product(shirt_color, shirt_size))

print(shirt_pairs)


# Example for the chain
# list1 = [1, 2, 3]
# list2 = [4, 5, 6]

# for num in chain(list1, list2):
#     print(num)

# features = ["A", "B", "C"]

# all_subsets = chain.from_iterable(
#     combinations(features, r)
#     for r in range(len(features) + 1)
# )

# print(list(all_subsets))

features = ["Age", "Salary", "Experience", "Education"]

powerset = chain.from_iterable(
    combinations(features, r) for r in range(len(features) + 1)
)

for subset in powerset:
    print(subset)
