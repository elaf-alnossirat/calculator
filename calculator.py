1# Calculator with History Feature

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b1

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

def calculate(operation, a, b):
    if operation == '+':
        return add(a, b)
    elif operation == '-':
        return subtract(a, b)
    elif operation == '*':
        return multiply(a, b)
    elif operation == '/':
        return divide(a, b)
    else:
        return "Error: Invalid operation."

# Function to display the history
def show_history(history):
    if not history:
        print("No history to show.")
    else:
        print("\nHistory:")
        for entry in history:
            print(entry)

# Function to clear history
def clear_history():
    return []

# Main program
def main():
    history = []
    while True:
        print("\n--- Calculator ---")
        print("1. Perform a calculation")
        print("2. View history")
        print("3. Clear history")
        print("4. Exit")
        choice = input("Choose an option (1-4): ")

        if choice == '1':
            try:
                num1 = float(input("Enter the first number: "))
                operation = input("Enter the operation (+, -, *, /): ")
                num2 = float(input("Enter the second number: "))

                result = calculate(operation, num1, num2)
                if "Error" not in str(result):
                    history.append(f"{num1} {operation} {num2} = {result}")
                print(f"Result: {result}")
            except ValueError:
                print("Error: Invalid number input. Please try again.")
        elif choice == '2':
            show_history(history)
        elif choice == '3':
            history = clear_history()
            print("History cleared.")
        elif choice == '4':
            print("Exiting the calculator. Goodbye!")
            break
        else:
            print("Invalid option. Please choose 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()


