"""
Name: functions.py
Author: itsf4llofstars
Desc: Functions file for Python3
"""


def add_two_numbers(num1, num2):
    return num1 + num2


def main():
    a, b = 12, 34
    c, d = 12.34, 56.78

    print(add_two_numbers(a, b))
    print(add_two_numbers(c, d))


if __name__ == "__main__":
    main()
