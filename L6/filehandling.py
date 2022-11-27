def main():
    with open("szoveg.txt", "r") as f, open("masolat.txt", "w") as out:
        for line in f:
            out.write(line)



if(__name__ == "__main__"):
    main()