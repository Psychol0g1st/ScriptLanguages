def is_palindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

if __name__ == "__main__":
    text = input("Adj meg szoveget: ")
    print("Palindrom" if is_palindrome(text) else "Nem palindrom")
    