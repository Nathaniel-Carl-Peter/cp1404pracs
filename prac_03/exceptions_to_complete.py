"""
CP1404/CP5632 - Practical
Fill in the TODOs to complete the task
"""

is_finished = False
while not is_finished:
    try:
        result = int(input("Valid int: "))
        is_finished = False
    except ValueError:  # TODO - add the exception you want to catch after except
        print("Enter valid integer.")  # Triggers when user input  is not an integer
print(f"Valid result is {result}")
