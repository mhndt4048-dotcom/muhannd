# Simple Calculator - Python Beginner Project

print("=== Simple Calculator ===")

while True:
    try:
        first_number = float(input("Enter the first number: "))
        operator = input("Enter operator (+, -, *, /): ")
        second_number = float(input("Enter the second number: "))

        if operator == "+":
            result = first_number + second_number
        elif operator == "-":
            result = first_number - second_number
        elif operator == "*":
            result = first_number * second_number
        elif operator == "/":
            if second_number == 0:
                print("Error: Cannot divide by zero.")
                continue
            result = first_number / second_number
        else:
            print("Invalid operator.")
            continue

        print("Result:", result)

        again = input("Do you want to calculate again? (y/n): ").lower()
        if again != "y":
            print("Goodbye!")
            break

    except ValueError:
        print("Please enter valid numbers.")
