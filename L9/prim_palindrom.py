import math

def is_palindrom(s: str) -> bool:
	return s == s[::-1]

def is_prime(num: int) -> bool:
	if num < 2:
		return False

	for i in range(2, num//2):
		if num % i == 0:
			return False
	return True

def test(num: int) -> int:
	iterator: int = num
	while not (is_prime(iterator) and is_palindrom(str(iterator))):
		iterator += 1;
	return iterator

def main() -> None:
	num: int = int(input("Addj meg egy szamot:"))
	print(f"test({num}) == {test(num)}")

if __name__ == "__main__":
	main()