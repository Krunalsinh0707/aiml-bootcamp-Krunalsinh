# print(name)
# NameError: name 'name' is not defined 

# name = "Krunalsinh"
# print(name/2)

#TypeError: unsupported operand type(s) for /: 'str' and 'int'

# lst=[1,2,3]
# print(lst[3])

#IndexError: list index out of range

# print(10/0)
# ZeroDivisionError: division by zero

# dict_01={
#     "Name":'Krunalsinh',
#     "Age": 21
# }

# print(dict_01["Email"])

# KeyError: 'Key not found in dictionary'

try:
    print(10/0)
except ZeroDivisionError:
    print("You cannot divide by zero")