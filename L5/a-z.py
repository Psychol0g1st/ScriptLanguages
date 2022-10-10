#!/usr/bin/env python3
# encoding: utf-8
import sys

def abc():
    """
    Fuggveny amely visszateriti az angol abc-t egy stringben
    """
    buffer = ['a']
    i = 0
    while buffer[i] != 'z':
        buffer.append(chr(ord(buffer[i]) + 1))
        i += 1
    return buffer

def main():
    if sys.argv[0] == 'z-a.py':
        print("".join(abc()[::-1]))    
    else:
        print("".join(abc()))    



if(__name__ == "__main__"):
    main()