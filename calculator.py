a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
opr = input("Enter the operation (+, -, *, /): ")

if opr == "+":
    result = a + b
elif opr == "-":
    result = a - b
elif opr == "*":
    result = a * b
elif opr == "/":
    result = a / b
else:
    result = "Invalid operation"

print("Your answer is:", result)

  
  

  
