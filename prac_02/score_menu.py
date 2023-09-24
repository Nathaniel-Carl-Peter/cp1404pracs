"""
CP1404 - Score Menu

Pseudo:

display menu
get user input

"""


def main():
    """Score Menu function"""
    MENU = "Menu:\n(V)alid score\n(S)tars\n(Q)uit"
    print(MENU)
    choice = input(">>> ").upper()
    while choice != 'Q':
        if choice == 'V':
            score = get_valid_score()
            determined_score(score)
        elif choice == 'S':

        else:
            print("Invalid choice :P")
        print(MENU)
        choice = input(">>> ").upper()
    print("Farewell friend. ;)")


def get_valid_score():
    """Get a valid score between 0 - 100"""
    score = float(input("Enter score: "))
    return score


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
