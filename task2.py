def calculator():
    # Prompt the user for input
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    
    print("Select the operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    
    operation = input("Enter the operation as per (1/2/3/4): ")
    
    # Perform the calculation based on user input
    if operation == '1':
        result = num1 + num2
        print(f"Here is your result for the operation performed : {num1} + {num2} = {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"Here is your result for the operation performed : {num1} - {num2} = {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"Here is your result for the operation performed : {num1} * {num2} = {result}")
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"Here is your result for the operation performed : {num1} / {num2} = {result}")
        else:
            print("Error! Division by zero is not allowed.")
    else:
        print("Invalid operation choice!")

# Run the calculator
calculator()