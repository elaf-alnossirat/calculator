def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error: Cannot divide by zero"

def power(x, y):
    return x ** y


def calculator():
    history = []  # List to store the history of operations

    while True:
        print("""
        ------------------- MENU -------------------
        1. Add
        2. Subtract
        3. Multiply
        4. Divide
        5. View History
        6. Clear History
        7. Exit
        ------------------------------------------
        """)

        choice = input("Enter choice (1-7): ")

        if choice == '5':
            print("\nHistory of operations:")
            if history:
                for operation in history:
                    print(operation)
            else:
                print("No operation performed yet.")
            continue

        if choice == '6':
            history.clear()
            print("History has been cleared.")
            continue

        if choice == '7':
            print("Exiting calculator. Goodbye!")
            break

        if choice not in ['1', '2', '3', '4']:
            print("Invalid input. Please select a valid option.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = add(num1, num2)
                operation = f"{num1} + {num2} = {result}"
            elif choice == '2':
                result = subtract(num1, num2)
                operation = f"{num1} - {num2} = {result}"
            elif choice == '3':
                result = multiply(num1, num2)
                operation = f"{num1} * {num2} = {result}"
            elif choice == '4':
                result = divide(num1, num2)
                operation = f"{num1} / {num2} = {result}"

            print(operation)
            history.append(operation)

        except ValueError:
            print("Error: Invalid input. Please enter valid numbers.")

        continue_choice = input("Do you want to perform another operation? (yes/no): ")
        if continue_choice.lower() != 'yes':
            break

    print("\nFinal History of operations:")
    if history:
        for operation in history:
            print(operation)
    else:
        print("No operation performed.")

# Call the calculator function to run the program
calculator()
