final_num = 0
num1 = float(input("What is your first number:"))
num2 = float(input("What is your second number:"))
operator = input ("what would you like to do to the numbers: (+,-,x,/)")

if operator == "+":
    final_num = num1 + num2
elif operator == "-":
    final_num = num1 - num2
elif operator == "x":
    final_num = num1 * num2
elif operator == "/":
    final_num = num1 / num2
else:
    print ("Invalid operator")
print (final_num)