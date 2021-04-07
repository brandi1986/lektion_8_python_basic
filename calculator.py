var1 = int(input("Number 1:"))
operation = input("Operator:")
var2 = int(input("Number 2:"))


if operation == "+":
    result = var1 + var2
    print(result)
elif operation == "-":
    result = var1 - var2
    print(result)
elif operation == "*":
    result = var1 * var2
    print(result)
elif operation == "/":
    result = var1 / var2
    print(result)
else:
    print("Wrong input!!!")
