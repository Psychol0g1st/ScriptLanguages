#!/usr/bin/env python3

def main():
    szamok_negyzeteinek_osszege = sum([num**2 for num in range(1,11)])
    szamok_osszegeinek_negyzete = sum([num for num in range(1,11)])**2
    print("Elso tiz szam szamok negyzeteinek osszegenek es szamok osszegeinek negyzetenek kulonbsege: ", szamok_osszegeinek_negyzete - szamok_negyzeteinek_osszege)
#############################################################################

if __name__ == "__main__":
    main()