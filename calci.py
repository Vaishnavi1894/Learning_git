print("This is a Calculator Program:")
a=int(input("Enter a:"))
b=int(input("Enter b:"))
operation = input("Enter the Operation you need to perform:")
def calculator():
    if operation == "add":
        print(a+b)
    else:
        print(a-b)
    
calculator()

