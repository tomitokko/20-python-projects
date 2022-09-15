def main():
    email_input = input("Input your email address: ")

    (username, domain) = email_input.split("@")
    (domain, extension) = domain.split(".")

    print("Username :" , username)
    print("Domain :", domain)
    print("Extension :", extension)

    print("")
    replay = input("Still Wanna Play ? (y/n) ") # Ask Wanna PLay again ? Give option to continue play or not
    if replay == "Y" or replay == "y":
        main()

print("Welcome to the email slicer ")
print("")

main()
