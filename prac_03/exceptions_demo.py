"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
    When the user input is not an integer
2. When will a ZeroDivisionError occur?
    Occurs if the denominator is 0 and only
3. Could you change the code to avoid the possibility of a ZeroDivisionError?
    
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))
    fraction = numerator / denominator
    print(fraction)
except ValueError:  # Occurs when user inputs are not integers
    print("Numerator and denominator must be valid numbers!")
except ZeroDivisionError:  # Occurs when denominator is = 0
    print("Cannot divide by zero!")
print(f"")
print("Finished.")
