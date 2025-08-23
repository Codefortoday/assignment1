try:
    with open("sampl.txt","r") as f1:
        print("Reading file contains:")
        print("Line 1:",f1.readline())
        print("Line 2:",f1.readline())
except FileNotFoundError:
    print("Error:The expected file not found")
