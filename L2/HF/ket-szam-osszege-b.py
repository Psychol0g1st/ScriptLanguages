def osszeg(a,b):
    return a + b
def main():
    num1 = int(input("Add meg az elso szamot: "))
    num2 = int(input("Add meg a masodik szamot: "))
    print("{} + {} = {}".format(num1, num2, osszeg(num1, num2)))

if __name__ == "__main__":
    main()