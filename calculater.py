first = float(input("Enter the first number =>"))
second = float(input("Enter the second number =>"))
opr = str(input("Enter operation (+,-,*,/) =>"))

if opr == "+":
    total = first + second

elif opr == "-":
    total = first - second

elif opr =="*":
    total = first * second

elif opr == "/":
    total = first / second

else: 
    total=str("Please enter a valid operation")
print("The result is:", total)

