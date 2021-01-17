def day_of_moth(*args, **kwargs):
    for m in args:
        month = get_month_name(int(m))
        print(month, end=' ')
    for key in kwargs.keys():
        print("has number of days: ", kwargs[key], end=' ')
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
    day_of_moth("1", "3", "5", "7", "8", "10", "12", dom=31)
    day_of_moth("2", dom=28)
    print("In leap year", end=' ')
    day_of_moth("2", dom=29)
    day_of_moth("4", "6", "9", "11", dom=30)


if __name__ == '__main__':
    main()
