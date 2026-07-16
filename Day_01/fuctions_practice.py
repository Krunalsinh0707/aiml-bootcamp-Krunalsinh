def greet(name = "Guest"):
    return f"Hello {name}!"

print(greet("Krunalsinh"))
a=[]

def average(a):
    if len(a)==0:
        return 0
    
    return sum(a)/len(a)
print(average(a))