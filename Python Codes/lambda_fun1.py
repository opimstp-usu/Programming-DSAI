"""
Filename: lambda_fun.py
Demonstrate the use of lambda function
"""
import random

def create_random(count):
    rand_list = []
    for i in range(count):
        r = random.randint(0, 100)
        rand_list.append(r)

    return(rand_list)


def checkprime(x):
    rem = 0
    if int(x) > 2:
        for i in range(2, int(x)):
            if int(x) % i == 0:
                rem = 1
                break
    elif int(x) == 2:
        rem = 0
    else:
        rem = 1
    return rem


def main():
    one_list = create_random(10)
    some_list = list(map(lambda x: checkprime(x), one_list))
    zero_list = list(filter(lambda x: x == 0, some_list))
    one_list = list(filter(lambda x: x == 1, some_list))
    print("{} is prime".format(prime_list))
    print("{} is not prime".format(non_prime_list))


if __name__ == '__main__':
    main()
