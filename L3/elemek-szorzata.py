from unittest import result


def main():
    numbers = [1,5,3]
    result = product(numbers)
    print(numbers, end=" ")
    print("lista elemeinek szorzata: {}".format(product([])))

def product(numbers):
    result = 1
    for number in numbers:
        result *= number
    return result

if __name__ == "__main__":
    main()