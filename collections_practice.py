names = ["asha", "ravi", "asha", "meera", "ravi"]

# unique_names = []
# for n in names:
#     if n not in unique_names:
#         unique_names.append(n)
unique_names=list(dict.fromkeys(names))
unique_names1 = list(set(names))
print(unique_names)
print(unique_names1)
name_len = {name: len (name) for name in dict.fromkeys(names)}
print(name_len)


a=[8,88,9,3,4,22,100,910]

largest_num = max(a)
smallest_num = min(a)
average = sum(a)/len(a)
print(f"Largest number is {largest_num} and smallest number is {smallest_num}")
print(f"Average of the numbers is {average}")


#Tuple is used when we want to store the data which is not going to change in future. It is immutable.
