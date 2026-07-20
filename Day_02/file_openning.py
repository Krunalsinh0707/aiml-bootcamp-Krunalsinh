with open("big.txt") as f:
    # for i in range(1,500001):
    #     f.write(f"{i}The Life is Fine\n")
    content=f.read()
    count=0
    counts=0
    for line in f :
        count+=1

        if "Fine" in line:
            counts+=1
    
        

print(count)
print(counts)
# print(content)    