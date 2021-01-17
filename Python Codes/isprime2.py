"""
Filename: isprime2.py
Only allow integer input
"""
def get_integer_input(message):
    """
    If user enters other than numbers, input will be rejected
    """
    valstr = input(message)
    #print(type(valstr))
    while not valstr.isnumeric():
        print("Input must be integer!")
        valstr = input(message)
    return int(valstr)

def checkprime(x):
    rem = 0
    for i in range(2, x):
        if x % i == 0:
            print("Divided by {}".format(i))
            rem = 1
            break
    return rem


def main():
    x = get_integer_input("Please give an integer: ")
    #print(type(x))
    if x <= 1:
        print("Smallest prime is 2.")
    else:
        rem = checkprime(x)
        if rem != 0:
            print("{} is not prime".format(x))
        else:
            print("{} is prime.".format(x))

if __name__ == '__main__':
    main()
