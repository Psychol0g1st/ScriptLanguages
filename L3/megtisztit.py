def clean_wia_split(text):
    return "".join(text.split())

def clean_wia_replace(text):
    return text.replace(" ", "").replace("\n", "").replace("\t", "")

def main():
    print(clean_wia_replace("192.168.0.1: \n6666"))

if __name__ == "__main__":
    main()