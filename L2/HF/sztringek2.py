# coding: utf-8

# Copyright 2010 Google Inc.
# Licensed under the Apache License, Version 2.0
# http://www.apache.org/licenses/LICENSE-2.0

# Google's Python Class
# http://code.google.com/edu/languages/google-python-class/

# A magyar változatot készítette:
# Szathmáry László (jabba.laci@gmail.com)
# frissítés Python 3-ra: 2016.09.09.

# További sztring műveletek

from operator import not_


def verbing(s):
    if s.endswith('ing'):
        s = s + 'ly'
    elif len(s) >= 3:
        s = s + 'ing'

    return s

def not_bad(s):
    not_i = s.find('not')
    bad_i = s.find('bad')
    if not_i < bad_i:
        return s[: not_i] + "good" + s[bad_i+3 :]
    return s

def front_back(a, b):
    a_begin = a[:len(a)//2]    
    a_end = a[len(a)//2:]
    if len(a) % 2 != 0:
        a_begin = a[:len(a)//2+1]
        a_end = a[len(a)//2+1:]
    b_begin = b[:len(b)//2]    
    b_end = b[len(b)//2:]
    if len(b) % 2 != 0:
        b_begin = b[:len(b)//2+1]
        b_end = b[len(b)//2+1:]
            
    
    return a_begin + b_begin + a_end + b_end


# Egy egyszerű teszt fv. Kiírja az egyes fv.-ek visszaadott értékét, ill.
# azt is, hogy mit kellett volna visszaadniuk.
def test(got, expected):
    if got == expected:
        prefix = ' OK '
    else:
        prefix = '  X '
    print('{p} got: {g}; expected: {e}'.format(p=prefix, g=got, e=expected))


# Ezt ne módosítsuk.
# A main() fv. meghívja a fenti fv.-eket különféle paraméterekkel,
# s a test() fv. segítségével megnézi, hogy az eredmények helyesek-e.
def main():
    print('verbing')
    test(verbing('hail'), 'hailing')
    test(verbing('swiming'), 'swimingly')
    test(verbing('do'), 'do')

    print()
    print('not_bad')
    test(not_bad('This movie is not so bad'), 'This movie is good')
    test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
    test(not_bad('This tea is not hot'), 'This tea is not hot')
    test(not_bad("It's bad yet not"), "It's bad yet not")

    print()
    print('front_back')
    test(front_back('abcd', 'xy'), 'abxcdy')
    test(front_back('abcde', 'xyz'), 'abcxydez')
    test(front_back('Kitten', 'Donut'), 'KitDontenut')

#############################################################################

if __name__ == '__main__':
    main()
