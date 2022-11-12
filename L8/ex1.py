#!/usr/bin/env python3
# encoding: utf-8
import pygyak

def main():
    print([i for i in range(200) if pygyak.is_prime(i)]) 


if(__name__ == "__main__"):
    main()