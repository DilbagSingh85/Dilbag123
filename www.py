file= open("teams.txt","r")

print("First line: ")
print(file.readline())
print("second line:")
print(file.readline())
print("Rest of file:")
print(file.read())

file.close()
