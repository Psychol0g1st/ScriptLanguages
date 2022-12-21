#!/usr/bin/env python3
# encoding: utf-8

import sys


def main():
    if len(sys.argv) == 4:
        words = [set(word) for word in sys.argv[1:]]
        intersect = words[0].intersection(words[1]).intersection(words[2])
        ordered = sorted(list(intersect))
        print("Közös karakterek: ", end="")
        if len(ordered) > 0:
            print(", ".join(ordered))
        else:
            print("--")
    else:
        print("Adj meg pontosan 3 parancssori argumentumot!")


if __name__ == "__main__":
    main()
