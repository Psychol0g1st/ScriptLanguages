#!/usr/bin/env python3
# encoding: utf-8

class Greetings(object):
    def __init__(self, name):
        self.name = name
    def say_hi(self):
        print(f"Hi {self.name}!")

def main():
    g = Greetings("Alice") 
    g.say_hi()

if(__name__ == "__main__"):
    main()