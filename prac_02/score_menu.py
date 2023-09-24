MENU = "Menu:\n(H)ello\n(G)oodbye\n(Q)uit"
name = input("Enter name: ")
print(MENU)
choice = input(">>> ").upper()
while choice != 'Q':
    if choice == 'H':
        print("Hello", name)
    elif choice == 'G':
        print("Goodbye", name)
    else:
        print("Invalid choice :P")
    print(MENU)
    choice = input(">>> ").upper()
print("Finished. ;)")
