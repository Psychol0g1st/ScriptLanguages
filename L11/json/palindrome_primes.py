#!/usr/bin/env python3
# encoding: utf-8

from typing import List, Any
import json


def read_from_json(filename: str) -> List[int]:
    with open(filename, "r") as file:
        data: str = file.read()
        return json.loads(data)


def is_palindrome(item: Any) -> bool:
    return str(item) == str(item)[::-1]


def get_quantity_of_palindrome_values(l: List[int], print_flag: bool = False) -> int:
    quantity: int = 0
    for item in l:
        if is_palindrome(item):
            quantity += 1
            if print_flag:
                print(item)
    return quantity


def main() -> None:
    primes: List[int] = read_from_json("primes.json")
    palindrome_quantity: int = get_quantity_of_palindrome_values(primes, True)
    print(f"Osszesen: {palindrome_quantity} palindrom prim van")


if __name__ == "__main__":
    main()
