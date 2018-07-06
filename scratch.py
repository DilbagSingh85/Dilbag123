# scratch
def volume(number1,number2,number3):
    if number1 < 0 or number2 < 0 or number3 < 0:
        print ("invalid input")
    else:
            volumevalue = number1*number2*number3
            print("volume: ", volumevalue)

length=float(input("enter length: "))
breadth=int(input("enter breadth: "))
height=int(input("enter height: "))

volume(length,breadth,height)

length2=float(input("enter length: "))
breadth2=int(input("enter breadth: "))
height2=int(input("enter height: "))

volume(length2,breadth2,height2)
#name of the procedure(parameters)
