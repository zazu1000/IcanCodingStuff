#1

# string = input("Write anything: ")

# print(string[::-1])

#2

# list1 = [1, 1, 3, 7, 10, 1, 5, 3, 8]
# final_list = []
# def unique(list):
#     for num in list:
#         if list.count(num) <= 1:
#             final_list.append(num)
#     print(final_list)

# unique(list1)

#3

true_list = [1, 1, 1, 2, 3, 4, 5, 4, 3, 2, 1]
false_list = [1, 1, 1, 2, 3, 4, 5, 4, 3, 2 ]

def true_or_false(list):

    for num in list:
        if list.count(num) < 3:
            true_false = False

        else:
            true_false = True

    print(true_false)

true_or_false(true_list)
true_or_false(false_list)

