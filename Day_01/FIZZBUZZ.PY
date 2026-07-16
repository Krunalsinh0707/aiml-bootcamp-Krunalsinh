# for n in range (1,101):
#     if n%3==0 and n%5==0:
#         print("FizzBuzz")
#         continue

#     if n%3==0:
#         print("Fizz")
#         continue
#     if n%5==0:
#         print("Buzz")
#         continue
#     print(n)

# print(list(range(0,101,10)))

starting_point = int(input('Enter The Starting Point'))
ending_point = int(input('Enter The Ending Point'))

divisor3 = 3
divisor5 = 5

word_for_num_div_by_3 = input('Enter The Word For Numbers Divisible By 3')
word_for_num_div_by_5 = input('Enter The Word For Numbers Divisible By 5')
full_word = word_for_num_div_by_3 + word_for_num_div_by_5

for ele in range(starting_point,(ending_point+1)):
  if ele %divisor3==0 and ele%divisor5 == 0:
    print(ele,full_word)
  elif ele % divisor3==0:
    print(ele,word_for_num_div_by_3)
  elif ele % divisor5==0:
    print(ele,word_for_num_div_by_5)