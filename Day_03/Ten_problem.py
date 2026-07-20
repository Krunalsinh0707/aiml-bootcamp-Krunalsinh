numbers=[1,2,3,4,5]

sq=[]

for n in numbers:
    if n%2==1:
        sq.append(n*n)

        
print ("Loop Squere",sq)

Com_sq=[n*n for n in numbers if n%2==1]

print("Comprehension Squere",Com_sq)

#2

names=["krunal" ,  "Yuvi" ,  "deepak" , "Harshil" ]

uppercase_name=[]

for n in names:
    cleaned=n.strip().upper()
    uppercase_name.append(cleaned)
print("Looped_uppercase-names",uppercase_name)

com_name=[n.strip().upper() for n in names]

print ("Comprehension Name" , com_name)


#3

list_01=[1,2,3,4,5]
list_02=[10,20,30,40,50]

product=[]

for n1,n2 in zip(list_01,list_02):
    product.append(n1*n2)

print("Looped product:" , product)

comp_product=[n1*n2 for n1,n2 in zip(list_01,list_02)]

print("Comprewhension Product:",comp_product)

#4

words = ["apple", "banana", "mango", "orange", "grapes"]

long_word=[]

for word in words:
    if len(word)>4:
        long_word.append(word)

comp_long_word=[word for word in words if len(word)>4]

print ("loop long Word:",long_word) 
print ("comp long Word:",comp_long_word) 

#5
from functools import reduce

list=[10,20,30,40,50]

product2=1

for n in list:
    product2*=n
print(product2)

product1=reduce(lambda x ,y : x * y ,list)

print(product1)
    
#6

items = [
    {"name": "apple", "price": 10},
    {"name": "banana", "price": 5},
    {"name": "mango", "price": 20}
]

total_price=0

for item in items:
    total_price=total_price + item["price"]
print("loop :",total_price)

total_prices=reduce(lambda total , item : total +item["price"],items,0)

print("reduce:",total_prices)

#7

nested_list=[[1,2],[3,4],[5]]

flatten_list=[]
for sublist in nested_list:
        for num in sublist:
            flatten_list.append(num)
print(flatten_list)

flatten_list_02=reduce(lambda x, y : x+y, nested_list )
print(flatten_list_02)

#8

words = ["apple", "banana", "mango", "orange"]

length_dict = {}

for word in words:
    length_dict[word] = len(word)

print(length_dict)

words = ["apple", "banana", "mango", "orange"]

com_length_dict = dict(map(lambda word: (word, len(word)), words))

print(com_length_dict)


#9

values = [0, 1, "", "Hello", None, [], [1, 2], False, True]

loop_value = []

for value in values:
    if value:
        loop_value.append(value)

print(loop_value)

values = [0, 1, "", "Hello", None, [], [1, 2], False, True]

comp_value= [value for value in values if value]

print(comp_value)

#10

numbers = [1, 2, 3]

loop_running_total = []
total = 0

for num in numbers:
    total += num
    loop_running_total.append(total)

print(loop_running_total)

comp_running_total = reduce(lambda acc, x: acc + [acc[-1] + x] if acc else [x],numbers,[])

print(comp_running_total)

