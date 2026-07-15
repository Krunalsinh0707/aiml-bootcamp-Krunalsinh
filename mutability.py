a=[1,2,3]

b = a.copy()
b.append(4)

print(a) #[1,2,3,4]
print(id(a)) #[1,2,3,4]
print(b)
print(id(b)) #[1,2,3,4]


# This Example is immutable

# c = 1,2 
# d = c

# d.append(3)

# print(c)
# print(d)
