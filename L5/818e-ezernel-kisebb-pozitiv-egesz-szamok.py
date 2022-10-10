#!/usr/bin/env python3
# encoding: utf-8
def ezernel_kisebb_pozitiv_egesz_szamok_osszege():
    """
    List comprehension segitsegevel 
    a fuggveny meghatatozza ezernel kisebb szamok 
    3 vagy 5 tobbszoroseinek az osszeget
    """
    result = sum([num for num in range(1000) if num % 3 == 0 or num % 5 == 0])
    print("1000-nel kisebb pozitiv egesz szamok 3 vagy 5 tobbszoroseinke osszege = ", result)


def main():
    ezernel_kisebb_pozitiv_egesz_szamok_osszege()


if(__name__ == "__main__"):
    main()