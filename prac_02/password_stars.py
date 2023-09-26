"""
CP1404 - Programing 2

Password Stars
"""

MINIMUM_LENGTH = 4


def original():
    """Get a password of valid size and print asterisks."""
    password = input(f"Enter password of at least 6 characters: ")
    while len(password) < 4:
        password = input(f"Enter password of at least 6 characters: ")
    print('*' * len(password))


def version_1():
    """Get a password of valid size and print asterisks."""
    password = input(f"Enter password of at least {MINIMUM_LENGTH} characters: ")
    while len(password) < MINIMUM_LENGTH:
        password = input(f"Enter password of at least {MINIMUM_LENGTH} characters: ")
    print('*' * len(password))


def main():
    password = get_password(MINIMUM_LENGTH)
    print_asterisk(password)


def get_password(minimum_length):
    password = input(f"Enter password of at least {minimum_length} characters: ")
    while len(password) < minimum_length:
        print("Password to short")
        password = input(f"Enter password of at least {minimum_length} characters: ")
    return password


def print_asterisk(sequence):
    print('*' * len(sequence))


# version_1()
# main()
original()
