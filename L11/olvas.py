import json

def main():
    fname = "person.json"
    with open(fname) as file:
        d = json.load(file)
        print(d)
        print(d['daughter']['salary'])


if(__name__ == "__main__"):
    main()