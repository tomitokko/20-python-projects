def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print('Leap Year' )
            else:
                print('Not leap year')
        else:
            print('Leap year' )
    else:
        print('Not Leap Year')

is_leap_year(2051)
