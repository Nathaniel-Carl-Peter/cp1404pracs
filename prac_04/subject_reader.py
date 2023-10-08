"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    subjects = get_subject()
    display_subjects(subjects)


def get_subject():
    """Read data from file formatted like: subject,lecturer,number of students."""
    subject = []
    input_file = open(FILENAME)
    for line in input_file:
        print(line)  # See what a line looks like
        print(repr(line))  # See what a line really looks like
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        print(parts)  # See what the parts look like (notice the integer is a string)
        parts[2] = int(parts[2])  # Make the number an integer (ignore PyCharm's warning)
        print(parts)  # See if that worked
        subject.append(parts)
        print("----------")
    input_file.close()
    return subject


def display_subjects(subjects):
    """Display subjects"""
    for subject in subjects:
        print(f"{subject[0]} is taught by {subject[1]:12} amd has {subject[2]:3} students")


main()

"""
Output:
CP1401 is taught by Ada Lovelace and has 192 students
CP1404 is taught by Alan Turing  and has  98 students
"""
