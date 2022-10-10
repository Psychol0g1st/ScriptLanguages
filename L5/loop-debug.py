#!/usr/bin/env python3
# encoding: utf-8

def loop(iterations, debug = False):
    """Kiir egy szamsorozatot az #iterations# parameterben megadott szamig.
    Rendelkezik #debug# parameter igaz ertek eseteben debug informaciot is ir ki."""
    if(debug):
        print("#ciklus kezdete")
    for i in range(1, iterations + 1):
        print(i, end=" ")

    print()
    if(debug):
        print("#ciklus vege")

def main():
    loop(5, debug=True)
    print("*"*20)
    loop(5)



if(__name__ == "__main__"):
    main()