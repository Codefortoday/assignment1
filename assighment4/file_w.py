a=(input("Enter text to entered to file: "))
try:
    with open("output.txt","w") as  file:
        if file.write(a):
            print("data successfully entered into the file.")
        else:
            print("cannot enter data")
except FileNotFoundError:
    print("File not found!")
    
b=input(("enter addtional text to append to file: "))
try:
    with open("output.txt","a") as  file1:
        if file1.write(b):
            print("data successfully appended into the file.")
        else:
            print("cannot enter data")
except FileNotFoundError:
    print("File not found!")
finally:
    with open("output.txt","r") as file2:
        print("final content of file:",file2.read())

