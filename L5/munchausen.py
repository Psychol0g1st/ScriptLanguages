#!/usr/bin/env python3
# encoding: utf-8
pwr = [0] * 10

def isMunchausen(number):
    """Eldonti parameterben megkapot szamrol hogy muncahusen szam-e."""
    sum = 0
    temp = number
    while(temp > 0 and sum <= number):
        sum = sum + pwr[(temp % 10)]
        temp = temp // 10
    return sum == number

def print_all_munchausen_numbers(limit):
    """Kiirja az osszes munchausen szamot parameterben megadott szamig."""
    for i in range(1,10):
        pwr[i] = i ** i
    for i in range(limit):
        if(isMunchausen(i)):
            print(i)

def main():
    print_all_munchausen_numbers(440_000_000)

if(__name__ == "__main__"):
    main()