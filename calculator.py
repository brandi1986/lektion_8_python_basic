var1 = input("Number 1:")
operation = input("Operator:")
var2 = input("Number 2:")


if operation == "+":
    result = int(var1) + int(var2)
    print(result)
elif operation == "-":
    result = int(var1) - int(var2)
    print(result)
elif operation == "*":
    result = int(var1) * int(var2)
    print(result)
elif operation == "/":
    result = int(var1) / int(var2)
    print(result)
else:
    print("Wrong input!!!")