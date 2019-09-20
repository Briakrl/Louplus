#!/usr/bin/env python3

import sys

def calc(income1):
    insurance = income1 * 0.165
    income2 = income1 - 5000 - insurance
    if income2 <= 0:
        tax = 0
    elif income2 <= 3000 and income2 > 0:
        tax = income2 * 0.03
    elif income2 > 3000 and income2 <= 12000:
        tax = income2 * 0.1 - 210
    elif income2 > 12000 and income2 <= 25000:
        tax = income2 * 0.2 -1410
    elif income2 > 25000 and income2 <= 35000:
        tax = income2 * 0.25 - 2660
    elif income2 > 35000 and income2 <= 55000:
        tax = income2 * 0.3 - 4410
    elif income2 > 55000 and income2 <= 80000:
        tax = income2 * 0.35 - 7160
    else:
        tax = income2 * 0.45 - 15160
    income3 = income1 - insurance - tax
    return income3

def main():
    for arg in sys.argv[1:]:
        id, x = arg.split(':')
        try:
            income = float(x)
            if income < 0:
                raise ValueError("Parameter Error")
                continue
            print("{}:{:.2f}".format(id, calc(income)))
        except ValueError:
            print("Parameter Error")

if __name__ == '__main__':
    main()
