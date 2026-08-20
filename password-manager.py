print("Welcome to the password manager!\n")

print("Security Disclaimer")

print("This is an educational project and should not be used to store real passwords or other sensitive information.")

print("Passwords are stored in a plain .txt file and are not encrypted. This means that anyone who gains access to the file can read the stored passwords.\n")


def create_password():
    name = input('enter your name for password: ')
    password = input(' enter your password: ')
    description = input(' description for your password: ')

    try:
        pass_folder = open("password.txt", "a")
        pass_folder.write(f"{name}, {password}, {description}\n")
        pass_folder.close()
    except OSError:
        print("Error: could not save the password.")

    return name, password, description


def read_password():
    try:
        with open("password.txt", "r", encoding="cp1251") as pass_folder:
            content = pass_folder.read()

        return content

    except FileNotFoundError:
        print("Error: password.txt was not found.")
        return ""


while True:
    while True:
        print("0. Exit from Program")
        print("1. Add password")
        print("2. Find password")
        print("3. clear all passwords")

        try:
            user_input = int(input("Enter your choice: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        if user_input == 0:
            exit()

        if user_input == 1:
            print('1. create a new password:')
            print('2. exit')

            try:
                number = int(input('Please enter the number: '))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if number == 1:
                create_password()

            elif number == 2:
                break

            else:
                print("Please enter a valid choice.")

        elif user_input == 2:
            count = read_password()
            names = count.splitlines()

            print("0. Exit")

            for number, name in enumerate(names, start=1):
                name_number = name.split(",")[0]
                print(f"{number}. {name_number}")

            try:
                find_num = int(input("write your choice:"))
            except ValueError:
                print("Please enter a valid number.")
                continue

            if find_num == 0:
                break

            try:
                print(f"\n{names[find_num - 1]}\n")
            except IndexError:
                print("There is no password with this number.")

        elif user_input == 3:
            print('Are you sure? (yes/no)')
            answer = input("Enter your answer: ")

            if answer == "yes":
                try:
                    with open("password.txt", "w") as file:
                        pass
                    print("All passwords have been cleared.")
                except OSError:
                    print("Error: could not clear the passwords.")

            elif answer == "no":
                continue

            else:
                print("Please write yes or no.")

        else:
            print("Please enter a valid choice.")
