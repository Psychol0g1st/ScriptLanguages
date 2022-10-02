#!/usr/bin/env python3

def xor(str1, str2):
    return bool(str1) and not bool(str2)

def main():
    print("str1: \"python\" -- str2: None")
    print(xor("python", None))
    print("str1: None -- str2: None")
    print(xor(None, None))
    print("str1: \"\" -- str2: None")
    print(xor("", None))
    print("str1: None -- str2: \"Python\"")
    print(xor(None, "Python"))
    print("str1: True -- str2: None")
    print(xor(True, None))
#############################################################################

if __name__ == "__main__":
    main()