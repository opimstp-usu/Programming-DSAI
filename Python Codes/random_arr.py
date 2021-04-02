"""
Filename: random_arr.py
Importing random library
"""
import random

def create_random_array(num_arr):
    myArr = []
    for i in range(num_arr):
       myArr.append(random.randint(1,num_arr))
    return myArr

def print_arr(num_arr):
	for num in num_arr:
		print("{} ".format(num), end=' ')

def main():
    x = input("Please give an integer: ")
    my_arr = create_random_array(int(x))
    print_arr(my_arr)

if __name__ == '__main__':
    main()