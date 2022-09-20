def szam_fordit(num):
    return int(str(num)[::-1])
def main():
    number = input("Adj meg egy szamot: ")
    print("{} -> {}".format(number, szam_fordit(number)))

if __name__ == "__main__":
    main()