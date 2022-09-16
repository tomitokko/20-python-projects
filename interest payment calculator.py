def main():
    print("This is monthly loan calculator")
    print("")

    principal = float(input("Input The Loan Amount: "))
    apr = float(input("Input The Annual Interest Rate: "))
    years = int(input("Input Amount Of Years: "))

    monthly_interest_rate = apr / 1200
    amount_of_months = years * 12
    monthly_payment = principal * monthly_interest_rate / (1-(1 + monthly_interest_rate) ** (-amount_of_months))

    print("The monthly payment for this loan is : $ %.2f " % monthly_payment)

    play = input("Still Wanna Count? (y/n) ") # made some replay count again
    if play == "Y" or play == "y":
        main()

main()

