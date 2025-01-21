def calculate():
    expression = input("""
                      °--------------------------°
                      |                          | 
                      | Enter the expression:    |
                      | Example: 3 + 5 * 2       |
                      |                          |
                      °--------------------------°              
                       << Expression >>:   """)
    
    try:
        result = evaluate_expression(expression)
        print(f"Result: {result}")
        save_to_history(expression, result)
    except Exception as e:
        print(f"Error: {e}. Please enter a valid expression.")
    
    again()

def evaluate_expression(expression):
    import re
    tokens = re.findall(r'\d+\.\d+|\d+|[+\-*/()]', expression.replace(' ', ''))
    
    def precedence(op):
        if op in ('+', '-'):
            return 1
        if op in ('*', '/'):
            return 2
        return 0

    def apply_operation(operators, values):
        right = values.pop()
        left = values.pop()
        op = operators.pop()

        if op == '+':
            values.append(left + right)
        elif op == '-':
            values.append(left - right)
        elif op == '*':
            values.append(left * right)
        elif op == '/':
            if right == 0:
                raise ValueError("Division by zero")
            values.append(left / right)

    values = []
    operators = []

    for token in tokens:
        if token.isnumeric() or '.' in token:
            values.append(float(token))
        elif token == '(':
            operators.append(token)
        elif token == ')':
            while operators and operators[-1] != '(':
                apply_operation(operators, values)
            operators.pop()
        else:
            while (operators and precedence(operators[-1]) >= precedence(token)):
                apply_operation(operators, values)
            operators.append(token)

    while operators:
        apply_operation(operators, values)

    return values[0]

def save_to_history(expression, result):
    with open("history.txt", "a") as file:
        file.write(f"{expression} = {result}\n")

def show_history():
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
    with open("history.txt", "w") as file:
        pass  # Open in write mode to overwrite and clear the file
    print("Calculation history has been cleared.")        

def again():
    calculate_again = input('''
    Do you want to:
    1. Calculate again? press (Y)
    2. View calculation history? press (H)
    3. Clear calculation history? press (C)
    4. Exit? press (N)
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
        print("Invalid input. Please type Y, H, C, or N.")
        again()

# Start the program
calculate()
