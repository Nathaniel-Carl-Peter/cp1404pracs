"""
CP1404/CP5632 - Practical
Pseudocode for temperature conversion

display menu
get_choice
while choice != "Q":
    if choice == "C":
        get_celsius
        fahrenheit = celsius * 9.0 / 5 + 32
        display fahrenheit
    elif choice == "F":
        get_fahrenheit
        celsius = 5 / 9 * (fahrenheit - 32)
        display celsius
    else:
        display Invalid option
    print(MENU)
    get_choice
display end message
"""


def main():
    MENU = """C - Convert Celsius to Fahrenheit
    F - Convert Fahrenheit to Celsius
    Q - Quit"""
    print(MENU)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            get_celsius()
        elif choice == "F":
            get_fahrenheit()
        else:
            print("Invalid option")
        print(MENU)
        choice = input(">>> ").upper()
    print("Thank you.")


def get_celsius():
    """Convert to celsius"""
    celsius = float(input("Celsius: "))
    fahrenheit = celsius * 9.0 / 5 + 32
    print(f"Result: {fahrenheit:.2f} F")


def get_fahrenheit():
    """Convert to fahrenheit"""
    fahrenheit = float(input("Fahrenheit: "))
    celsius = 5 / 9 * (fahrenheit - 32)
    print(f"Result: {celsius:.2f} C")


main()
