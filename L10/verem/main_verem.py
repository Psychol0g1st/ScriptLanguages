# encoding: utf-8
from typing import Any
from Verem import Verem

def main() -> None:
    v: Verem = Verem()      # üres verem létrehozása
    print(v)         # [
    print(v.ures())  # True
    v.betesz(1)
    v.betesz(4)
    v.betesz('Text')
    print(v)         # [1 4 5
    print(v.meret()) # 3
    print(v.ures())  # False
    x: Any = v.kivesz()    # 5
    print(v)
    print(x)         # [1 4
    v.kivesz()
    v.kivesz()       # most már üres
    x = v.kivesz()
    print(x)

if __name__ == "__main__":
    main()