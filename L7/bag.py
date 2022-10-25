#!/usr/bin/env python3
# encoding: utf-8

from typing import List


class Bag(object):
    def __init__(self):
        self.data = []
    def add(self, value):
        self.data.append(value)
    def __str__(self):
        return f"Bag: {self.data}"
    def add_twice(self, value):
        self.add(value)
        self.add(value)

def main():
    b = Bag()
    b.add(3)
    b.add(5)
    b.add_twice(6)
    print(b)
if(__name__ == "__main__"):
    main()