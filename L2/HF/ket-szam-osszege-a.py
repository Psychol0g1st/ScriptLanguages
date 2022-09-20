import sys
def osszeg(a,b):
    return a + b

def main():
    if(len(sys.argv) == 3):
        num1 = int(sys.argv[1])
        num2 = int(sys.argv[2])
        print("{} + {} = {}".format(num1, num2, osszeg(num1, num2)))
    else:
        print("Adj meg pontosan 2 szamot parancssori argumentum kent!")

if __name__ == "__main__":
    main()
        