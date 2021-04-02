"""
Filename: list_prime.py
List a limited number of prime numbers
"""
def get_integer_input(message):
    """
    If user enters other than numbers, input will be rejected
    """
    valstr = input(message)
    while not valstr.isnumeric():
        print("Input must be integer!")
        valstr = input(message)
    return int(valstr)

def get_prime(n):
    prim = []
    for p in range(2, n):
        rem = 2
        pp = True
        while rem < p:
            if p % rem == 0:
                pp = False
            rem += 1
        if (pp == True):
            prim.append(p)
    return prim

def main():
    n = get_integer_input("Please give a limit: ")
    if n <= 0:
        print("Limit must be non negative.")
    else:
        prim = get_prime(n)

    print("List of prime numbers: {}".format(prim))
    print("There are {} prime numbers less than {}".format(len(prim), n))

if __name__ == '__main__':
    main()