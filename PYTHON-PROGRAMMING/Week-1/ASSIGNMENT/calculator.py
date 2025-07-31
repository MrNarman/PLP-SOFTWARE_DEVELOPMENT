print("Welcome to the Calculator!")

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))
operation = input("Enter the operation (+, -, *, /): ")

if operation == '+':
    print("The result is: ", first_number + second_number)
elif operation == '-':
    print("The result is: ", first_number - second_number)
elif operation == '*':
    print("The result is: ", first_number * second_number)
elif operation == '/':
    if second_number != 0:
        result = first_number / second_number
    else:
        print("Error: Division by zero is not allowed.")
else:
    print("Error: Invalid operation. Please enter +, -, *, or /.")


