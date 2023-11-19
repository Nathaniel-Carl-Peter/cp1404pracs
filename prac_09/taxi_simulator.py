from prac_09.car import Car
from prac_09.taxi import Taxi
from prac_09.silver_service_taxi import
def main():
    """Main taxi program"""
    total_bill = 0
    print("Let's drive")
    MENU = "q)uit, c)hoose taxi, d)rive"
    print(MENU)
    choice = input(">>> ").upper()
    while choice != 'q':
        if choice == 'c':
            print("Hello")
        elif choice == 'd':
            print("Goodbye")
        else:
            print("Invalid choice :P")
        print(MENU)
        choice = input(">>> ").upper()
    print("Finished. ;)")
