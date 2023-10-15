"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
# https://peps.python.org/pep-0020/
# Boundary conditions should be checked (e.g. >= 50 should be considered a passing score not > 50)
# If condition should have an else condition at the last path
# Use fewer if/elif condition
# Flat is better than nested quote from "The Zen of Python".
# There is only one path condition for "Invalid score" (DRY principle)

"""
Pseudo:
get_score
if score < 0 or > 100:
    display Invalid score
else if score >= 90:
    display Excellent
else if score >= 50:
    display Passable
else
    display Bad
"""


def main():
    """Function get score"""
    score = float(input("Enter score: "))
    determined_score(score)


def determined_score(score):
    """Function determined score"""
    if score < 0 or score > 100:
        print("Invalid score")
    elif score >= 90:
        print("Excellent")
    elif score >= 50:
        print("Passable")
    else:
        print("Bad")


main()
