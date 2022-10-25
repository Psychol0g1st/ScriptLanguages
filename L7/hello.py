#!/usr/bin/env python3
# encoding: utf-8

class Hello:

    def create_name(self, name):
        self.name = name
    def display_name(self):
        return self.name
    def print_name(self):
        print(self.name)
    def greet(self):
        print(f"Hi {self.name}!")


def main():
    h = Hello()
    print(h.name)
    h.create_name("Alice")
    h.print_name()
    print(h.display_name())
    h.greet()
if(__name__ == "__main__"):
    main()