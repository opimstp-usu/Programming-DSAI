"""
Filename: display_date.py
Displaying date with named arguments
"""
def mydate(message, d = 1, m=1, y=2000):
    month = get_month_name(int(m))
    date = str(d) + ' ' + month + ' ' + str(y)
    print(message, date)


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
    mydate("Year of millennium")
    mydate(message="Happy New Year", y=2021)


if __name__ == '__main__':
    main()
