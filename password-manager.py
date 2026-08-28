print("Welcome to the password manager!\n")

print("Security Disclaimer")

print("This is an educational project and should not be used to store real passwords or other sensitive information.")

print("Passwords are stored in a plain .txt file and are not encrypted. This means that anyone who gains access to the file can read the stored passwords.\n")


def create_password():
    name = input('enter your name for password: ')
    password = input(' enter your password: ')
    description = input(' description for your password: ')

    try:
        with open("password.txt", "a", encoding="cp1251") as pass_folder:
            pass_folder.write(f"{name}|{password}|{description}\n")
    except OSError:
        print("Error: could not save the password.")




def read_password():
    try:
        with open("password.txt", "r", encoding="cp1251") as pass_folder:
            content = pass_folder.read()

        return content

    except FileNotFoundError:
        print("Error: password.txt was not found.")
        return ""


def create_new_password():
    print('1. create a new password:')
    print('2. exit')

    try:
        enter_number = int(input('Please enter the number: '))
    except ValueError:
        print("Please enter a valid number.")
        return

    if enter_number == 1:
        create_password()

    elif enter_number == 2:
        return

    else:
        print("Please enter a valid choice.")

def remover():
    print('1. choose to delete a password')
    print('2. clear all passwords')
    try:
     choose = int(input("enter your choice: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    if choose == 1:

        count = read_password()
        count_line = count.splitlines()

        for number, line in enumerate(count_line, start=1):
            name_number = line.split("|")[0]
            print(f"{number}. {name_number}")

        try:
            delete_num = int(input("Enter the number that you want to delete: "))
        except ValueError:
            print("Please enter a valid number.")
            return

        if 1 <= delete_num <= len(count_line):
            try:
                with open("password.txt", "w") as file:
                    for i, line in enumerate(count_line, start=1):
                        if i != delete_num:
                            file.write(line + "\n")

                print(f"Password number {delete_num} has been deleted.")
            except OSError:
                print("Error: could not delete the password.")
        else:
            print("There is no password with this number.")

    elif choose == 2:

        print('Are you sure? (yes/no)')
        answer = input("Enter your answer: ")

        if answer == "yes":
            try:
                with open("password.txt", "w"):
                    pass
                print("All passwords have been cleared.")
            except OSError:
                print("Error: could not clear the passwords.")

        elif answer == "no":
            return

        else:
            print("Please write yes or no.")

    else:
      print("Please enter a valid choice.")

def find_password():
    content = read_password()
    count_lines = content.splitlines()
    print("0. Exit")

    for numbering, lines in enumerate(count_lines, start=1):
        names_number = lines.split("|")[0]
        print(f"{numbering}. {names_number}")

    try:
        find_num = int(input("write your choice:"))
    except ValueError:
        print("Please enter a valid number.")
        return

    if find_num == 0:
        return

    if 1 <= find_num <= len(count_lines):
        print(f"\n{count_lines[find_num - 1]}\n")
    else:
        print("There is no password with this number.")

while True:

        print("0. Exit from Program")
        print("1. Add password")
        print("2. Find password")
        print("3. Delete password")

        try:
            user_input = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if user_input == 0:
            print("goodbye! See you next time)")
            exit()

        if user_input == 1:
            create_new_password()

        elif user_input == 2:
            find_password()


        elif user_input == 3:
            remover()
