class Dog:
    name = "Doggy"

    def __init__(self, age):
        self.age = age

def main():
    dog1 = Dog(23)
    dog2 = Dog(21)

    print(dog1.age)
    print(dog1.name)
    dog1.name = "dfafsadf"
    print(dog1.name)
    print(dog2.age)
    print(dog2.name)

if __name__ == "__main__":
    main()