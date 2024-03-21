print("Yo")

#String
#any grouping of characters inside of ""
x = "Ex: Hows it gong"
print (x)

#BooLean
#True or False
x = True
x = False
if x:
    print("Hello")
else:
    print("World")

#Float
#Any number with a decimal point
x = 5.5

#Integer
#Any whole number
x = 5

#Character/Char
#A single character inside ''
x = 'a'

#Converting
x = 5
x = str(x)
x = int(x)
x = float(x)
x = bool(x)

#inputs
name = input("Write your name: ")
print("Your name is " + name)

#==
#Equals
#!=
#Does not equal
#>=
#Greater than or equal to
#<=
#Less than or equal to

#modulo %
#   11 % 2 = 1

num1 = float(input("What is your first number:"))
num2 = float(input("What is your second number:"))

final_num = num1 % num2
if final_num == 0:
    num1 = str(num1)
    num2 = str(num2)
    print(num1 + " is divisble by " + num2 )
else:
    final_num = str(final_num)
    print("Your numbers are not divisible, the remainder is: " + final_num)