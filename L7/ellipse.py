#!/usr/bin/env python3
# encoding: utf-8
import math
class Ellipse:
    def __init__(self, length_x, length_y):
        self._length_x = length_x
        self._length_y = length_y
    def perimeter(self):
        return math.pi*(self._length_x + self._length_y)
    def area(self):
        return math.pi * self._length_x * self._length_y
    def get_length_x(self):
        return self._length_x
    def get_length_y(self):
        return self._length_y
    def __str__(self):
        return f"Ellipse({self._length_x}, {self._length_y})"
    def __bool__(self):
        return self._length_x > 0 and self._length_y > 0
def main():
    e1 = Ellipse(5, 2.5)
    e2 = Ellipse(2.7, 7.1)

    if e1: # s1.__bool__() értéke alapján dönti el
        print("e1 igaznak számít")
    else:
        print("e1 hamisnak számít")
    print("-" * 20)
    print(f"{str(e1)} area: {e1.area()}")
    print(f"{str(e2)} perimeter: {e2.perimeter()}")

if(__name__ == "__main__"):
    main()