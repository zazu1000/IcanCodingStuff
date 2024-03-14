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
def num_line():
    first_num = int(input("First number: "))
    second_num = int(input("Second number: "))

    times = second_num - first_num + 1

    if first_num > second_num:
        for i in range(times):
            print(first_num)
            first_num = first_num + 1
    
    

num_line()