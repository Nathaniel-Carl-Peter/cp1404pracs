# Program out put name

out_file = open("name.txt", "w")
name = input("Enter name: ").title()
print(name, file=out_file)
out_file.close()

# Name Program version 2
with open(f"name.txt", 'r') as in_file:
    name = in_file = in_file.read().strip()
print(f" Your name is ... {name}")

# File Program numbers

in_file = open("numbers.txt", "r")
number_1 = int(in_file.readline())
number_2 = int(in_file.readline())
in_file.close()
print(number_1 + number_2)

# File Program numbers 2

in_file = open("numbers.txt", "r")
total = 0
for line in in_file:
    number = int(line)
    total += number
in_file.close()
print(total)
