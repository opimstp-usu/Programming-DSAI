# This is a a program to count number of primes generated within a three-dimensional array.

import numpy as np

class MyNumpy:

    def __init__(self):
        self.myarr = np.random.randint(100, size=(3, 4, 5))

    def print_myarr(self):
        # Use a breakpoint in the code line below to debug your script.
        for i in range(3):
            for j in range(4):
                for k in range(5):
                    print(self.myarr[i,j,k], end=' ')  # Press Ctrl+F8 to toggle the breakpoint.
                print()
            print()
        print()

    def count_prime(self):
        n = 0
        for i in range(3):
            for j in range(4):
                for k in range(5):
                    if (self.myarr[i,j,k] > 1):
                        pr = self.check_prime(self.myarr[i,j,k])
                        if pr == 0:
                            print(self.myarr[i,j,k], end=' ')
                            n += 1
        return n

    def check_prime(self, x):
        rem = 0
        for i in range(2, x):
            if x % i == 0:
                rem = 1
                break
        return rem

def main():
    mynum = MyNumpy()
    mynum.print_myarr()
    num_prime = mynum.count_prime()
    print('There are ', num_prime, ' prime numbers generated.')

if __name__ == '__main__':
    main()
