"""
Filename: repeatchars.py
Repeatedly displaying characters with default parameter
"""

def repeat_chars(ch='*', number=5):
    for i in range(number):
        print(ch, end=' ')
    print()

def main():
    repeat_chars()
    repeat_chars('#')
    repeat_chars('%', 15)

if __name__ == '__main__':
    main()