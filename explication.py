# Code Explanation:
# 1. Function Definition
# python

# def save_to_history(x, y, operation, result):
# This defines a function named save_to_history that:
# Takes four inputs: x, y, operation, and result.
# These are the numbers, the mathematical operation, and the result of the calculation.
# 2. Docstring
# python

# """Save the operation and result to a history file."""
# This is a comment (docstring) explaining what the function does:
# It saves the operation (e.g., 5 + 3 = 8) to a file called history.txt.
# 3. Open the File
# python

# with open("history.txt", "a") as file:
# This opens (or creates, if it doesn’t exist) a file named history.txt:
# The "a" mode means append. Any new data will be added to the end of the file without overwriting existing content.
# as file: The file is referred to as file within this block of code.
# 4. Write to the File
# python

# file.write(f"{x} {operation} {y} = {result}\n")
# This writes a line to the file using formatted text:
# Example: If x = 5, operation = "+", y = 3, and result = 8, the line will be:

# 5 + 3 = 8
# \n adds a new line so that each calculation is saved on a separate line.
# In Simple Words:
# The function saves a record of a calculation (like 5 + 3 = 8) to a text file called history.txt. It:

# Opens the file in append mode.
# Writes the numbers, operation, and result in a readable format.
# Closes the file automatically when done (because of with).
# This allows the program to keep a permanent record of all calculations. 😊




# Code Breakdown:
# 1. Function Definition
# python

# def show_history():
# This defines a function named show_history that:
# Reads the history.txt file.
# Displays all previous calculations saved in the file.
# 2. Docstring
# python

# """Display the history of calculations."""
# A comment explaining the purpose of the function: It displays the list of past calculations.
# 3. Print a Header
# python

# print("\nCalculation History:")
# Prints a header to indicate that the calculation history will follow.
# The \n adds a blank line above for better readability.
# 4. Try-Except Block
# python

# try:
# This block handles potential errors when trying to read the history.txt file.
# 5. Open the File
# python

# with open("history.txt", "r") as file:
# Opens the history.txt file in read mode ("r").
# If the file doesn’t exist, a FileNotFoundError will be raised, and the program will handle it in the except block.
# 6. Read the File
# python

# history = file.readlines()
# Reads all lines from the file into a list called history.
# Each line in the file becomes an item in the list.
# 7. Check if History Exists
# python

# if history:
# Checks if the history list contains any lines.
# If yes, it means there are saved calculations.
# 8. Print Each Line
# python

# for line in history:
#     print(line.strip())
# Loops through each line in the history list.
# line.strip() removes any extra spaces or newline characters for clean display.
# Example: If the file contains:

# 5 + 3 = 8
# 10 - 2 = 8
# It will print:

# 5 + 3 = 8
# 10 - 2 = 8
# 9. Handle Empty File
# python

# else:
#     print("No calculations found in history.")
# If the file exists but is empty, it displays a message indicating no calculations are found.
# 10. Handle Missing File
# python

# except FileNotFoundError:
#     print("No history file found. Start by performing a calculation.")
# If the history.txt file doesn’t exist, it informs the user to perform a calculation first (so the file gets created).
# In Simple Words:
# This function reads and displays past calculations from history.txt.
# If the file doesn’t exist, it tells the user to perform a calculation first.
# If the file is empty, it informs the user that no history is available.
# This makes the program user-friendly and ensures error handling for missing or empty files! 😊






