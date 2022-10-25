#!/usr/bin/env python3
# encoding: utf-8

class Verem:
    def __init__(self):
        self._values = []

    def __str__(self):
        return f"{self._values}"[:-1]
    def ures(self):
        return len(self._values) == 0
    def betesz(self, value):
        self._values.append(value)
    def kivesz(self):
        if(not self.ures()):
            return self._values.pop()
        else:
            return None
    def meret(self):
        return len(self._values)
def main():
    v = Verem()      # üres verem létrehozása
    print(v)         # [
    print(v.ures())  # True
    v.betesz(1)
    v.betesz(4)
    v.betesz(5)
    print(v)         # [1 4 5
    print(v.meret()) # 3
    print(v.ures())  # False
    x = v.kivesz()
    print(x)         # 5
    print(v)         # [1 4
    v.kivesz()
    v.kivesz()       # most már üres
    x = v.kivesz()
    print(x)      

if __name__ == "__main__":
    main()