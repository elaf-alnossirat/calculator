def calculate():
    operation = input("""Enter the oparation:
                      (+) for addition
                      (-) for subtraction
                      (*) for multiplication
                      (/) for division
                      operation: """)
    x = float(input("Enter the first number: "))
    y = float(input("Enter the second number: "))
    
    
        
    if operation == "+":
      print(f'{x}+{y}={x + y}')
      
    elif operation == "-":
      print(f'{x}-{y}={x - y}')
    elif operation == "*":
      print(f'{x}*{y}={x * y}')
    elif operation == "/":
      if y == 0:
        print("Division by zero is not allowed. Please try again.")
      else:
        print(f'{x}/{y}={x / y}')   
    else:
      print(" you did not enter a valid operation ,please try again")
    # Add again() function to calculate() function
    again()  
  
  
def again():
    calculate_again = input('''
    Do you want to calculate again?
    Please type Y for YES or N for NO.
    ''') 
    
    if calculate_again.upper() == "Y" :
      calculate()
    elif calculate_again.upper() == "N":
      print("see you later :)")
    else:
      again()           
calculate()                