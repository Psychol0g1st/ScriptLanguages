#!/usr/bin/env python3
# encoding: utf-8

import math

FILENAME = "input.txt"


def is_square(num):
    root = math.sqrt(num)
    return num == int(root + 0.5) ** 2


def main():
    with open(FILENAME, "r") as file:
        lines = file.read().split()
        code = {}
        for line in lines:
            num, s = line.split(";")
            if is_square(int(num)):
                code[int(num)] = s[0]
        keys = sorted(code.keys())
        message = "".join([code[i] for i in keys]).replace('_', ' ')
        print(message)


if __name__ == "__main__":
    main()
