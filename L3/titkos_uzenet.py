#!/usr/bin/env python3
# encoding: utf-8

from curses.ascii import isalnum
from dataclasses import replace
from operator import index, indexOf
import string

"""
Edes
"""

CODE = """
Cbcq Dgyk!

Dmeybh kce cew yrwyg hmrylyaqmr:
rylsjb kce y Nwrfml npmepykmxyqg lwcjtcr!

Aqmimjjyi:

Ynyb
"""

def main():
    alphabet = list(string.ascii_lowercase)
    solution = ""
    for i in range(len(CODE)):
        char = CODE[i]
        if char.isalpha():
            lower_letter = char.lower()
            if lower_letter in alphabet:
                letter_index = alphabet.index(lower_letter) + 2
                new_letter_index = (letter_index - len(alphabet)) if letter_index >= len(alphabet) else letter_index 
                solution += alphabet[new_letter_index] if char.islower() else alphabet[new_letter_index].upper()
        else:
            solution += char
            
    print(solution)



if(__name__ == "__main__"):
    main()