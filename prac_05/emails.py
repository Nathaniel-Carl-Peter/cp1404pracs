def main():
    """Main email program"""
    email_to_names = {}
    email = input(f"Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input(f"is your name {name}? (Y/N) ")
        if confirmation.upper() != "Y" and confirmation.upper() != "":
            name = input("Name: ")
        email_to_names[email] = name
        email = input(f"Email: ")

    for email, name in email_to_names.items():
        print(f"{name} ({email})")


def get_name_from_email(email):
    """Determined if email is in list"""
    prefix = email.split('@')[0]
    parts = prefix.split('.')
    name = " ".join(parts).title()
    return name


main()
"""
Output:

Email: lindsay.ward@jcu.edu.au
Is your name Lindsay Ward? (Y/n)
Email: abe@gmail.com
Is your name Abe? (Y/n) y
Email: jimbo546@hotmail.com
Is your name Jimbo546? (Y/n) no
Name: Jim Boh
Email: 

Lindsay Ward (lindsay.ward@jcu.edu.au)
Abe (Abe@gmail.com)
Jim Boh (jimbo546@hotmail.com)
"""
