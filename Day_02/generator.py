def fib_list(n):
    fib_seq = []
    a, b = 0, 1 
    for _ in range(n):
        fib_seq.append(a)
        a ,b=b, a+b
    return fib_seq



print(fib_list(10))    #[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

print(type(fib_list(10)))   #<class 'list'>


# n = int(input("Enter the number of Fibonacci numbers to generate: "))
def fib_gen(n):

    a, b = 0, 1
    for _ in range(n):
        print(yield a)
        a, b = b, a + b

    # a, b = 0, 1
    # for _ in range(n):
    #     yield a
    # a, b = b, a + b
        

print(list(fib_gen(10)))    #[0, 1, 1, 2, 3, 5, 8, 13, 21, 34]

print(type(fib_gen(10)))    #<class 'generator'>