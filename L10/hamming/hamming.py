

def hamming(str1: str, str2: str) -> int:
    distance: int = 0
    if(len(str1)!=len(str2)):
        return -1
    for i in range(len(str1)):
        if str1[i] != str2[i]:
            distance += 1
    return distance

def main() -> None:
    print(hamming('alma', 'tank'))
    print(hamming("toned", "roses"))
    print(hamming("toned", "toner"))
    print(hamming("anna", "anna"))



if __name__ == "__main__":
    main()