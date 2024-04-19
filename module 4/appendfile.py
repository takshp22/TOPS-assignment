file=open("T1.txt","a")
file.write("this is file management demo using python.\n")
file.close()
print("file written succesfully")


file=open("T1.txt","r")
print(file.read())
file.close()
