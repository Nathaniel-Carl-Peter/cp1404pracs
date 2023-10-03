def main():
    numbers = get_numbers()
    square_numbers(numbers)
    display_number(numbers)


def get_numbers():
    numbers = int(input(f"Enter numbers separated by commas: "))
    values = numbers.split(' , ')
    return numbers


def square_numbers(number):
    print("testing")


def display_number(numbers):
    """Display numbers"""
    print("test")


main()

# :D
