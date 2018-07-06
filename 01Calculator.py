# calculator ex

number1 = float(input("please enter first number: "))
number2 = float(input("please enter second number: "))

print("Menu: ")
print("1 - Add")
print("2 - subtract")
print("3 - multiply")
print("4 - divide")
print("5 - square")
print("6 - power")

menu_option = int(input("enter option: "))

if menu_option == 1:
    print(number1,"+",number2,"=",number1 + number2)
elif menu_option == 2:
    print(number1,"-",number2,number1 - number2)
elif menu_option == 3:
    print(number1,"*",number2,number1 * number2)
elif menu_option == 4:
    print(number1,"/",number2,number1 / number2)
elif menu_option == 5:
    print(number1,"squared",number2,number1 * number2)
elif menu_option == 6:
    print(number1,"to power of",number2,number1 * number2)

else:
    print("Invalid option selected")
