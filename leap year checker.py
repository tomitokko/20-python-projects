def is_leap_year(year):
    if year % 4 == 0 :
        if year % 100 == 0:
            if year % 400 == 0:
                print('Leap Year')
            else:
                print('Not Leap Year')
        else:
            print('Leap Year')
    else:
        print('Not Leap Year')

    
input_year = int(input('Input Year : ')) #made user input year
is_leap_year(input_year)

#code to replay again
while True:
    input_text = input('Still Wanna Input Year? (y/n) ')
    if input_text == 'Y' or input_text == 'y':
        input_year1 = int(input('Input Year : '))
        is_leap_year(input_year1)
    else:
        quit()

