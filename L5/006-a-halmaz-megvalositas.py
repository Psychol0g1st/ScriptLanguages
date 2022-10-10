#!/usr/bin/env python3
# encoding: utf-8

def remove_duplicates(l):
    """A fuggveny eltavolitja a parameterben megadott listaban az ismetlodo elemeket es rendezett listat add vissz"""
    d = {}
    for item in l:
        d[item] = None
    return sorted(d.keys())


def main():
    l = [5, 2, 3, 5, 1, 4, -200, 5, 1, 3, 2, 2, 5]
    print("elotte:")
    print(l)
    l = remove_duplicates(l)
    print("utanna:")
    print(l)

if(__name__ == "__main__"):
    main()