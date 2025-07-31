def basic_calculator():
    print("Welcome to the Basic Calculator!")
    print("Operations: + (addition), - (subtraction), * (multiplication), / (division)")
    
    try:
        # Get user input
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ").strip()
        
        # Perform calculation
        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                print("Error: Division by zero is not allowed!")
                return
            result = num1 / num2
        else:
            print("Invalid operation! Please enter one of: +, -, *, /")
            return
        
        # Display the result
        print(f"\nResult: {num1} {operation} {num2} = {result}")
    
    except ValueError:
        print("Error: Please enter valid numbers!")

# Run the calculator
if __name__ == "__main__":
    basic_calculator()