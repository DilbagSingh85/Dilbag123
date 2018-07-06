number1=input("please enter number1: ")
number2=input("please enter number2: ")

menu=["1.Add", "2.Subtract", "3.Multiply", "4.Divide", "5.Square", "6.Power"]
print(menu)

menu_option=int(input("pleae enter the menu_option: "))
if menu_option==1:
    print(number1,"+",number2,"=",number1 + number2)
elif menu_option==2:
     print(number1,"-",number2,"=",number1 - number2)
elif menu_option==3:
     print(number1,"*",number2,"=",number1 * number2)
elif menu_option==4:
     print(number1,"/",number2,"=",number1 / number2)
"""elif menu_option==5:
print(number1,"+",number2,"=",number1 + number2)
elif menu_option==2:
print(number1,"+",number2,"=",number1 + number2)"""
