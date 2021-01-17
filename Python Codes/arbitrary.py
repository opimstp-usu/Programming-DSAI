"""Function with arbitrary arguments
Filename: arbitrary.py
Supplying function with any number of arguments
"""

def any_date(*args):
    for date in args:
        one_date = date.split(" ")
        month = get_month_name(int(one_date[1]))
        the_date = one_date[0] + ' ' + month + ' ' +one_date[2]
        print(the_date, end = ' ')
    print()

def get_month_name(m):
    if m == 1:
        month = 'January'
    elif m == 2:
        month = 'February'
    elif m == 3:
        month = 'March'
    elif m == 4:
        month = 'April'
    elif m == 5:
        month = 'May'
    elif m == 6:
        month = 'June'
    elif m == 7:
        month = 'July'
    elif m == 8:
        month = 'August'
    elif m == 9:
        month = 'September'
    elif m == 10:
        month = 'October'
    elif m == 11:
        month = 'November'
    elif m == 12:
        month = 'December'
    else:
        month = 'Unknown'
    return month

def main():
    any_date("31 12 1960", "31 12 1970", "31 12 1980", "31 12 1990")
    any_date("1 1 2000", "1 1 2010", "1 1 2020")


if __name__ == '__main__':
    main()
