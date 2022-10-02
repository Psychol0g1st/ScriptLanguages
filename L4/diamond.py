#!/usr/bin/env python3

def diamond(height):
    if height % 2 == 0:
        print("Hiba! A magassag csak paros szam lehet!")
        exit(1)
    width = height*2
    for x in range(height):
        print(("*" * (2*x + 1)).center(width))
    for x in range(height - 2, -1, -1):
        print(("*" * (2*x + 1)).center(width))

def main():
    print("Diamond: 7")
    diamond(7)
    print("Diamond: 3")
    diamond(3)
    print("Diamond: 4")
    diamond(4)
#############################################################################

if __name__ == "__main__":
    main()