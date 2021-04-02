"""
Filename: string_arg.py
Call a function with string argument
"""

def my_function(str):
    str += "..."
    print(str)

def main():
    str = "Hello, world"
    my_function(str)
    print(str)

if __name__ == '__main__':
    main()