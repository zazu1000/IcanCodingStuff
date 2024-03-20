#1

# num = int(input("Input a number: "))
# exp = int(input("Input an exponent: "))
# number = 1

# for i in range(exp):
#     number = number * num

# print(number)


#2

# num_list = [1,2,3,4,5]
# x = 1

# for i in num_list:
#     print(i * x)
#     x = x * 10 + 1

#3

# def num_line():
#     first_num = int(input("First number: "))
#     second_num = int(input("Second number: "))

#     times = second_num - first_num + 1
#     times2 = first_num - second_num + 1

#     if first_num > second_num:
#         for i in range(times2):
#             print(second_num)
#             second_num = second_num + 1
#     else:
#         for i in range(times):
#             print(first_num)
#             first_num = first_num + 1
# num_line()

#4

# def prime_num():
#     first_num = int(input("First number: "))
#     if first_num < 2:
#         first_num = 2
#     second_num = int(input("Second number: "))
#     prime = 0
#     prime_nums = []
#     for num in range(first_num, second_num + 1):
#         if num > 3:
#             prime = 0
#             for i in range(2, num):
#                 if num % i == 0:
#                     break
#                 else:                 
#                     prime = prime + 1
#                     if prime > num / 2:   
#                         prime_nums.append(num)
#                         break
                    
#         else:
#             prime_nums.append(num)

#     print(prime_nums)
# prime_num()

#5

# def factorial():
#     number = int(input("Number: "))
#     final = 1

#     for i in range(number + 1):
#         if i > 1:
#             final = i * final
       
#     print(f"{number}! is {final}")

# factorial()