import string


def hello() -> int:
    return "hello"
age: int = "20"
name = "Antal"
apples = [1,2,5,7]
print(age)
print(type(apples))


print(hello())

brand = "amigoscode"
print("code" not in brand)

text = f"""
Hello {name}
How are yout?
I am {age} years old.
"""
print(text.format(name, age))