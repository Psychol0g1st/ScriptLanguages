#!/usr/bin/env python3
# encoding: utf-8

import json

def read_from_json(filename: str):
    with open(filename, 'r') as file:
        data: str = file.read()
        return json.loads(data)

def is_palindrome(item: str) -> bool:
    return str(item) == str(item)[::-1]

def get_quantity_of_palindrome_values(l, print_flag: bool = False) -> int:
    quantity: int = 0
    for item in l:
        if is_palindrome(item):
            quantity += 1
            if print_flag:
                print(item)
    return quantity

def main():
    primes = read_from_json('primek.json')
    palindrome_quantity: int = get_quantity_of_palindrome_values(primes, True)
    print(f"Osszesen: {palindrome_quantity} palindrom prim van")

if(__name__ == "__main__"):
    main()