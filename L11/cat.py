import sys

def cat(fname):
    try:
        with open(fname, 'r') as file:
            content = file.read()
            file.close()
            print(content)
    except FileNotFoundError as e:
        print(e)
def main():
    for arg in sys.argv[1:]:
        cat(arg)


if(__name__ == "__main__"):
    main()