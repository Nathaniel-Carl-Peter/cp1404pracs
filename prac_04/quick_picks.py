"""
CP1404 - Prac 04 - Quick Picks
Nathaniel Carl Peter

MAX = 45
NUMBER_OF_LINES = 6
MINIMUM = 1

def main:
get_number
while number_of_quick_numbers picks < 0:
    display Invalid
    get_number

for i in range(number_of_quick_numbers)
    quick_numbers = []
    for j in range(NUMBER_OF_LINES)
        number = random.randint(MINIMUM, MAXIMUM)
    quick_pick.append(number)
quick_picK.sort
"""

import random

NUMBER_OF_LINES = 6
MINIMUM = 1
MAX = 45


def main():
    """Quick number pick program"""
    number_of_quick_numbers = int(input("How many quick picks? "))
    while number_of_quick_numbers < 0:
        print("Invalid")
        number_of_quick_numbers = int(input("How many quick picks? "))
    for i in range(number_of_quick_numbers):
        quick_pick = []
        for j in range(NUMBER_OF_LINES):
            number = random.randint(MINIMUM, MAX)
            while number in quick_pick:
                number = random.randint(MINIMUM, MAX)
            quick_pick.append(number)
        quick_pick.sort()
    print(" ".join(f"{number:2}" for number in quick_pick))


"""
Output:

How many quick picks? 5
 1 12 14 15 30 36
 2  5  8 33 38 41
 2 12 19 22 29 43
13 21 28 29 42 43
 3  4 10 11 32 44
"""

main()
