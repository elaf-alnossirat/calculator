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
        return "Cannot divide by Zero"

def power(x, y):
    return x ** y
  
def remainder(x, y):
    return x % y

def calculator():
    history = []  # List to store the history of operations
  
    while True:
        print("\nSelect operation:")
        print("1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Power")
        print("6. Remainder")
        print("7. View History")
        print("8. Clear History")
        print("9. Reset History and Quit")

        choice = input("Enter choice 1/2/3/4/5/6/7/8/9: ")

        if choice == '9':
            print("Resetting history and exiting...")
            break

        if choice == '7':
            print("\nHistory of operations:")
            if history:
                for operation in history:
                    print(operation)
            else:
                print("No operation performed yet.")
            continue

        if choice == '8':
            history.clear()
            print("History has been cleared.")
            continue

        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = add(num1, num2)
                print(num1, "+", num2, "=", result)
                history.append(f"{num1} + {num2} = {result}")
            elif choice == '2':
                result = subtract(num1, num2)
                print(num1, "-", num2, "=", result)
                history.append(f"{num1} - {num2} = {result}")
            elif choice == '3':
                result = multiply(num1, num2)
                print(num1, "*", num2, "=", result)
                history.append(f"{num1} * {num2} = {result}")
            elif choice == '4':
                result = divide(num1, num2)
                print(num1, "/", num2, "=", result)
                history.append(f"{num1} / {num2} = {result}")
            elif choice == '5':
                result = power(num1, num2)
                print(num1, "**", num2, "=", result)
                history.append(f"{num1} ** {num2} = {result}")
            elif choice == '6':
                result = remainder(num1, num2)
                print(num1, "%", num2, "=", result)
                history.append(f"{num1} % {num2} = {result}")
            else:
                print("Invalid input")

        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")

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
