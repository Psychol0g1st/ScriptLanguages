#!/usr/bin/env python3
# encoding: utf-8

class Sor:
    def __init__(self):
        self._values = []

    def __str__(self):
        return f"{self._values}"[1:]
    def ures(self):
        return len(self._values) == 0
    def betesz(self, value):
        self._values.append(value)
    def kivesz(self):
        if(not self.ures()):
            return self._values.pop(0)
        else:
            return None
    def meret(self):
        return len(self._values)
def main():
    s = Sor()      # üres sor létrehozása
    print(s)         # ]
    print(s.ures())  # True
    s.betesz(1)
    s.betesz(4)
    s.betesz(5)
    print(s)         # 1, 4, 5]
    print(s.meret()) # 3
    print(s.ures())  # False
    x = s.kivesz()
    print(x)         # 1
    print(s)         # 4, 5]
    s.kivesz()
    s.kivesz()       # most már üres
    x = s.kivesz()
    print(x)      #None

if __name__ == "__main__":
    main()