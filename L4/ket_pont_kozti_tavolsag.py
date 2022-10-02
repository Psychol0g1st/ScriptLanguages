#!/usr/bin/env python3

import math

def distance(p1, p2):
    a = (p2[0] - p1[0])
    b = (p2[1] - p1[1])
    return math.sqrt(a*a + b*b)

def main():
    p1 = (1, 2)
    p2 = (6, 5)
    print("1. pont koordinatai: ",p1)
    print("2. pont koordinatai: ",p2)
    print('A ket pont kozti tavolsag: {:.2f}'.format(distance(p1, p2)))

#############################################################################

if __name__ == "__main__":
    main()