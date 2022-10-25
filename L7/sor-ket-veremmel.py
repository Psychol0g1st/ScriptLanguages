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
    def move_to(self, other):
        while(not self.ures()):
            other.betesz(self.kivesz())
class Sor:
    def __init__(self):
        self._vl = Verem()
        self._vr = Verem()

    def __str__(self):
        return f"{str(self._vl)}]"[1:]
    def is_empty(self):
        return self._vl.ures()
    def append(self, value):
        self._vl.betesz(value)
    def popleft(self):
        if(not self.is_empty()):
            self._vl.move_to(self._vr)
            temp = self._vr.kivesz()
            self._vr.move_to(self._vl)
            return temp
        else:
            return None
    def size(self):
        return self._vl.meret()
def main():
    s = Sor()      # üres sor létrehozása
    print(s)         # ]
    print(s.is_empty())  # True
    s.append(1)
    s.append(4)
    s.append(5)
    print(s)         # 1, 4, 5]
    print(s.size()) # 3
    print(s.is_empty())  # False
    x = s.popleft()
    print(x)         # 1
    print(s)         # 4, 5]
    s.popleft()
    s.popleft()       # most már üres
    x = s.popleft()
    print(x)      #None
if __name__ == "__main__":
    main()