#!/usr/bin/env python3
# encoding: utf-8

class Proba:
    i = 123

def main():
    print(Proba.i)
    ob = Proba()
    print(ob.i)
    ob.i = 1
    print(ob.i)
    print(Proba.i)


if(__name__ == "__main__"):
    main()