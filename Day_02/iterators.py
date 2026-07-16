it=iter([1,2,3,4,5])

while True:
    try:
        print(next(it))
    except StopIteration:
        break

with open("iterator.txt","r") as f:
    it=iter(f)
    while True:
        try:
            print(next(it))
        except StopIteration:
            break


# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))
# print(next(it))    stopiteration error will be raised because we have only 5 elements in the list