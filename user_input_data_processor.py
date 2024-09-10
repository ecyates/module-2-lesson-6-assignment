# 2. User Input Data Processor
# Objective: The aim of this assignment is to process and format user input data.

# Task 1: Input Length Validator 
# Write a script that asks for and checks the length of the user's first name and last name. 
# Both should be at least 2 characters long. If not, print an error message.

# Function takes two parameters (first and last name)
def valid_length(first_name, last_name):
    # Checks if the length meets the requirement (must be >= 2), else print an error statement
    if len(first_name) < 2 or len(last_name) < 2:
        print("ERROR: Both your first and last name must be at least 2 characters.")

# Check the function
valid_length('Elizabeth', 'Yates') #no error
valid_length('E', 'Yates') #error
valid_length('Elizabeth', "Y") #error
valid_length('E', 'Y') #error
valid_length('El', "Ya") #no error