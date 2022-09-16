import string
import random

characters = list(string.ascii_letters + string.digits + "!@#$%^&*()")

def generate_password():
    password_length = int(input("How long would you like your password to be? "))

    random.shuffle(characters)

    password = []

    for x in range(password_length):
        password.append(random.choice(characters))

    random.shuffle(password)

    password = "".join(password)
    print(password)
    option = input("Do you still wanna generate a password? (y/n) ") # made option for replay game again
    if option == 'Y' or option == 'y':
        generate_password()
    elif option == 'N' or option == 'n':
        print('Program Ended')
        quit()
    else:
        print("Invalid input, please input Y or N")
        quit()
    
    
print('Welcome to Your Password Generator')
generate_password()
