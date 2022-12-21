#!/usr/bin/env python3
# encoding: utf-8

FILENAME = "input.txt"


def main():
    with open(FILENAME, "r") as file:
        skyscrapers = [int(value) for value in file.read().split()]
        quantity = 0
        for i in range(len(skyscrapers)):
            if i > 0:
                if skyscrapers[i] > skyscrapers[i - 1]:
                    quantity += 1
    print(quantity)


if __name__ == "__main__":
    main()
