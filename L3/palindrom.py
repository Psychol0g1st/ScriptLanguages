#!/usr/bin/env python3
# encoding: utf-8

def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]
def is_palindrome_iterative(s):
    s = s.replace(" ", "").lower()
    i=0
    j=len(s)-1
    while(i <= j):
        if(s[i] != s[j]):
            return False
        i += 1
        j -= 1
    return True

def is_palindrome_recursive(s):
    if len(s) == 0 or len(s) == 1:
        return True
    return s[0] == s[-1] and is_palindrome_recursive(s[1:-1])
    
def main():
    s = "indul a gorog aludni"
    s = s.replace(" ", "").lower()
    print(is_palindrome(s)) 
    print(is_palindrome_iterative(s)) 
    print(is_palindrome_recursive(s)) 

    print(s)

if(__name__ == "__main__"):
    main()