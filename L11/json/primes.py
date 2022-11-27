#!/usr/bin/env python3
# encoding: utf-8

import json
from math import sqrt
import sys

def get_primes_in_json(limit: int) -> str:
    l:list(bool) = [True]*limit
    for i in range(2,int(sqrt(limit))+1):
        if (l[i]):
            for j in range(i*i, limit, i):
                l[j] = False
    primes: list(int) = []
    for i in range(2,limit):
        if l[i]:
            primes.append(i)
    return json.dumps(primes)

def write_to_file(filename:str, data:str)->None:
    with open(filename, 'w') as file:
        file.write(data)

def main():
    if len(sys.argv) == 2:
        n: int = int(sys.argv[1])
        print("Primek generalasa...")
        print("Fajlba iras megkezdese...")
        primesJson = get_primes_in_json(n)
        write_to_file("primek.json", primesJson)
        print("Fajlba iras befejezve")

    else:
        print("Parancssori argumentumba adj meg pontosan egy szamot!")

if(__name__ == "__main__"):
    main()