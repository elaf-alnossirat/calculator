def calculate():
    operation = input("""Enter the operation:
                      (+) for addition
                      (-) for subtraction
                      (*) for multiplication
                      (/) for division
                      operation: """)
    
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    result = None

    if operation == "+":
        result = x + y
        print(f"{x} + {y} = {result}")
    elif operation == "-":
        result = x - y
        print(f"{x} - {y} = {result}")
    elif operation == "*":
        result = x * y
        print(f"{x} * {y} = {result}")
    elif operation == "/":
        if y == 0:
            print("Division by zero is not allowed. Please try again.")
        else:
            result = x / y
            print(f"{x} / {y} = {result}")
    else:
        print("You did not enter a valid operation. Please try again.")

    # Save the operation to history if a valid result exists
    if result is not None:
        save_to_history(x, y, operation, result)
    
    # Ask the user if they want to calculate again
    again()

def save_to_history(x, y, operation, result):
    """Save the operation and result to a history file."""
    with open("history.txt", "a") as file:
        file.write(f"{x} {operation} {y} = {result}\n")

def show_history():
    """Display the history of calculations."""
    print("\nCalculation History:")
    try:
        with open("history.txt", "r") as file:
            history = file.readlines()
            if history:
                for line in history:
                    print(line.strip())
            else:
                print("No calculations found in history.")
    except FileNotFoundError:
        print("No history file found. Start by performing a calculation.")
        
def clear_history():
    """Clear the history of calculations."""
    with open("history.txt", "w") as file:
        pass  # Open in write mode to overwrite and clear the file
    print("Calculation history has been cleared.")        

def again():
    calculate_again = input('''
    Do you want to:
    1. Calculate again? (Y)
    2. View calculation history? (H)
    3. Clear calculation history? (C)
    4. Exit? (N)
    ''').upper()
    
    if calculate_again == "Y":
        calculate()
    elif calculate_again == "H":
        show_history()
        again()
    elif calculate_again == "C":
        clear_history()
        again()    
    elif calculate_again == "N":
        print("See you later! :)")
    else:
        print("Invalid input. Please type Y, H, or N.")
        again()

# Start the program
calculate()
