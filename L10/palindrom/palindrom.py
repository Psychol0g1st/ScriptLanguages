def is_palindrom(s: str) -> bool:
    s = s.replace(" ", "").lower()
    return s == s[::-1]
def is_palindrom_iterative(s: str) -> bool:
    s = s.replace(" ", "").lower()
    i: int = 0
    j: int = len(s)-1
    while(i <= j):
        if(s[i] != s[j]):
            return False
        i += 1
        j -= 1
    return True

def is_palindrom_recursive(s: str) -> bool:
    s = s.replace(" ", "").lower()
    if len(s) == 0 or len(s) == 1:
        return True
    return s[0] == s[-1] and is_palindrom_recursive(s[1:-1])
    
def main() -> None:
    print("""
        Palindrom-e 3 módszerrel:
        1. Megfordítás szeleteléssel
        2. Iteratív
        3. Rekruzív
    """)
    s: str = input("Ajd meg szoveget: ")
    print("Palindrom" if is_palindrom(s) else "Nem palindrom") 
    print("Palindrom" if is_palindrom_iterative(s) else "Nem palindrom") 
    print("Palindrom" if is_palindrom_recursive(s) else "Nem palindrom") 


if(__name__ == "__main__"):
    main()