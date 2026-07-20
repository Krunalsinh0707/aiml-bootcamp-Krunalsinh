from collections import defaultdict,namedtuple,deque,Counter 

data = [
    ("IT", "Krunal"),
    ("HR", "Asha"),
    ("IT", "Rahul")
]

employees=defaultdict(list)

for dept,emp in data:
    employees[dept].append(emp)
print(dict(employees))

person = namedtuple("person",["name","age","city"])

data_01 = [
    ("Krunal", 22, "Rajkot"),
    ("Rahul", 25, "Ahmedabad")
]

people=[person(name , age, city)for name , age, city in data_01]

for p in people:
    print(p.city)
    print(p[2])
print(people)


search_history=deque(maxlen=5)

search_history.append("java")
search_history.append("C++")
search_history.append("JavaScript")
search_history.append("Go")
search_history.append("python")


search_history.append("Rust")

print(search_history)


from collections import Counter

text1 = "python java python sql"
text2 = "python c++ sql sql"

c1 = Counter(text1.split())
c2 = Counter(text2.split())

print("Counter01",c1)
print("Counter02",c2)

print(c1 - c2)    #Counter({'python': 1, 'java': 1}) SUBSTRACTION
print(c2 - c1)   #Counter({'c++': 1, 'sql': 1})   SUBSTRACTION
print(c1 & c2)    #Counter({'python': 1, 'sql': 1})  INTERACTION
print(c2 & c1)    #Counter({'python': 1, 'sql': 1}) INTERACTION
print(c1 | c2)    #UNION
print(c2 | c1)    #UNION