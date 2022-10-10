#!/usr/bin/env python3
# encoding: utf-8

def valid(text, chars=""):
    """
    A fuggveny kivalogadja a #text# parameterbol azokat a karakterek amelyek megtalalhatoak a #chars# parameterben
    """
    result = []
    if(chars == ""):
        return text[0]
    else:
        for char in text:
            if char in chars:
                result.append(char)
        return "".join(result)

def main():
    print("-"*10)
    print(valid("Barking!"))
    print(valid("KL754!", "0123456789"))
    print(valid("BEAN!", "abcdefghijklmnopqrstuvwxyz"))
    print("-"*10)



if(__name__ == "__main__"):
    main()