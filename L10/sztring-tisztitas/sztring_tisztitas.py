def clean_wia_split(text: str) -> str:
    return "".join(text.split())

def clean_wia_replace(text: str) -> str:
    return text.replace(" ", "").replace("\n", "").replace("\t", "")

def main() -> None:
    text: str = "192.168.0.1: \n6666"
    print("Eredeti sztring (Raw): " + text)
    print("\nreplace() segítségével:")
    print(clean_wia_replace(text))
    print("\nsplit() segítségével:")
    print(clean_wia_split(text))


if __name__ == "__main__":
    main()