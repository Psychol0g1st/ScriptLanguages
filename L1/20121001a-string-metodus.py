#!/usr/bin/env python3
# encoding: utf-8


from curses.ascii import isdigit


def main():
    name = input("Nev: ").strip()
    print(f'Hello {name}!')
    #Megtisztítja a stringet számoktól (kicseréli a számot egy üres stringre).
    s = "Sz2i3443a An2t1a56l, h2o09g0087y v1123a898gy?"
    for letter in s:
        if letter.isdigit():
            s = s.replace(letter, '')
    print(f'Clear message:\n{s}')

if(__name__ == "__main__"):
    main()