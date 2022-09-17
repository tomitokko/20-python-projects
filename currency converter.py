from lib2to3.pytree import convert


def main():
    print("This program convert US Dollar to Pounds Sterling, Rupiah, Yen and Yuan")
    print("Input converter kurs with small letter !!")
    print()

    dollars = eval(input("Enter amount in dollars: $ "))
    convert_kurs = input("Enter kurs you wanna know: ") # ask input for variant kurs
    

    #give option for just one kurs every turn
    if convert_kurs == "pounds":
        pounds = convert_to_pounds(dollars)
        print("That is", '{:,.2f}'.format(pounds), "pounds.") #add print yen, rupiah and yuan. Give slice for every million value
    elif convert_kurs == "rupiah":
        rupiah = convert_to_rupiah(dollars)
        print("That is", 'Rp. {:,.2f}'.format(rupiah)) #add print yen, rupiah and yuan. Give slice for every million value
    elif convert_kurs == "yen":
        yen = convert_to_yen(dollars)
        print("That is", '{:,.2f}'.format(yen), "yen.") #add print yen, rupiah and yuan. Give slice for every million value
    elif convert_kurs == "yuan":
        yuan = convert_to_yuan(dollars)
        print("That is", '{:,.2f}'.format(yuan), "yuan.") #add print yen, rupiah and yuan. Give slice for every million value
    else :
        print("You input wrong kurs!!")
        quit()
        
    #give option to replay program again
    print()
    input1 = input("Still wanna convert?(y/n) ")
    if input1 == 'y' or input1 == 'Y':
        main()
    else:
        quit()

#add rupiah, yuan, and yen function for every convert function
convert_to_pounds = lambda dollars: dollars * 0.87
convert_to_rupiah = lambda dollars: dollars * 14999.20
convert_to_yen = lambda dollars: dollars * 142.96
convert_to_yuan = lambda dollars: dollars * 6.98

main()
