class EmptyClass:
    pass

class MyClass:
    def hello(self):
        return "Hello world"

def main():
    obj = MyClass()
    print(MyClass.hello())



if __name__ == "__main__":
    main()