#!/usr/bin/env python3
# encoding: utf-8
import math
class Sphere:
    def __init__(self, radius):
        self._radius = radius
    def diameter(self):
        return 2 * self._radius
    def surface_area(self):
        return 4 * math.pi * (self._radius ** 2)
    def circumference(self):
        return 2 * math.pi * self._radius
    def volume(self):
        return (4 / 3) * math.pi * (self._radius ** 3)
    def get_radius(self):
        return self._radius
    def __str__(self):
        return "Sphere({r})".format(r=self._radius)
    def __bool__(self):
        return self._radius > 0
    def __lt__(self, other):
        return self._radius < other.get_radius()
    def __le__(self, other):
        return self._radius <= other.get_radius()
    def __gt__(self, other):
        return self._radius > other.get_radius()
    def __ge__(self, other):
        return self._radius >= other.get_radius()
def main():
    s1 = Sphere(5)
    s2 = Sphere(2.7)
    s3 = Sphere(2.7)
    s4 = Sphere(5.7)

    if s1: # s1.__bool__() értéke alapján dönti el
        print("s1 igaznak számít")
    else:
        print("s1 hamisnak számít")
    print("-" * 20)
    print(f"{str(s1)} volume: {s1.volume()}")
    print(f"{str(s1)} surface area: {s1.surface_area()}")
    print(f"{str(s1)} circumference: {s1.circumference()}")
    print(f"{str(s1)} diameter: {s1.diameter()}")
    print(f"{str(s1)} radius: {s1.get_radius()}")


    print(f"{str(s1)} < {str(s2)} : {s1 < s2}")
    print(f"{str(s2)} <= {str(s3)} : {s2 <= s3}")
    print(f"{str(s1)} > {str(s2)} : {s1 > s3}")
    print(f"{str(s4)} >= {str(s1)} : {s4 >= s1}")


if(__name__ == "__main__"):
    main()