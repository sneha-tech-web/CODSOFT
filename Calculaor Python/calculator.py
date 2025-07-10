def calculator():
    print("📟 Welcome to Python Calculator")
    print("\nAvailable operations:")
    print(" +  ➡ Addition")
    print(" -  ➡ Subtraction")
    print(" *  ➡ Multiplication")
    print(" /  ➡ Division")
    print(" %  ➡ Modulus")
    print(" // ➡ Floor Division")
    print(" ** ➡ Exponentiation")

    try:
        num1 = float(input("\nEnter the first number: "))
        num2 = float(input("Enter the second number: "))
        operator = input("Choose an operation (+, -, *, /, %, //, **): ")

        if operator == '+':
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
        elif operator == '-':
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        elif operator == '*':
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")
        elif operator == '/':
            if num2 != 0:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
            else:
                print("Error: Division by zero.")
        elif operator == '%':
            result = num1 % num2
            print(f"Result: {num1} % {num2} = {result}")
        elif operator == '//':
            result = num1 // num2
            print(f"Result: {num1} // {num2} = {result}")
        elif operator == '**':
            result = num1 ** num2
            print(f"Result: {num1} ** {num2} = {result}")
        else:
            print("Invalid operator selected.")
    except ValueError:
        print("Invalid input. Please enter numeric values.")

# Run the calculator
calculator()