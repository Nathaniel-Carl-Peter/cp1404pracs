REQUIRED_LENGTH = 6


def original():
    password = input("Enter at least 6 characters: ")
    while len(password) < 6:
        print("Too short")
        password = input("Enter at least 6 characters: ")
    print(len(password) * '*')


def main():
    password = get_password(REQUIRED_LENGTH)
    print_stars(password)


def get_password(required_length):
    password = input("Enter at least 6 characters: ")
    while len(password) < required_length:
        print("Too short")
        password = input("Enter at least 6 characters: ")
    return password


def print_stars(sequence):
    print('*', len(sequence))


# original()
main()
