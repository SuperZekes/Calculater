num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))

print("What operation would you like to perform?")
print("1 - Addition") 
print("2 - Subtraction")
print("3 - Multiplication")
print("4 - Division")

choice = input("Enter choice (1/2/3/4): ")

if choice == '1':
    result = num1 + num2
elif choice == '2':
    result = num1 - num2
elif choice == '3':
    result = num1 * num2
elif choice == '4':
    if num2 == 0:
        print("Cannot divide by 0")
        result = "Undefined"
    else:
        result = num1 / num2
else:
    print("Invalid choice")
    
print("Result:", result)