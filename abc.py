file = open("xyz.txt","r")
print("first line:")
print(file.readline())
file.seek(0)
print("first line again")
print(file.readline())
file.seek(25,0)
print("from the 25th character....")
print(file.read())

file.close()

