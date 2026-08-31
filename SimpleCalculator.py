Num1=float(input("Enter First number:"))
Num2=float(input("Enter Second number:"))
print("\nChoose an operation:")
print("ADDITION(+)")
print("SUBSTRACTION(-)")
print("MULTIPLICATION(*)")
print("DIVISION(/)")
operation=input("Enter operation:")
if operation == "+":
    result=Num1 + Num2
elif operation == "-":
    result=Num1 - Num2
elif operation == "*":
    result=Num1 * Num2
elif operation == "/":
    if Num2 != 0:
        result= Num1 / Num2
    else:
        print("Cannot Divide by zero")
else:
    result="Invalid OPERATION"
print("RESULT:",result)