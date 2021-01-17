"""
Filename: isprime.py
Determine if a number is prime or not
"""
def checkprime(x):
    rem = 0
    for i in range(2, int(x)):
        if int(x) % i == 0:
            rem = 1
            break
    return rem


def main():
    x = input("Please give an integer: ")
    print(type(x))
    if int(x) <= 1:
        print("Smallest prime is 2.")
    else:
        rem = checkprime(x)
        if rem != 0:
            print("{} is not prime".format(x))
        else:
            print("{} is prime.".format(x))


if __name__ == '__main__':
    main()

