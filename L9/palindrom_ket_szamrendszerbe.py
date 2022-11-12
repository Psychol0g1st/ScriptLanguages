LIMIT: int = 1_000_000

def is_palindrom(s: str) -> bool:
	return s == s[::-1]

def dec_to_bin(num: int) -> str:
	return bin(num).replace("0b", "")


def main() -> None:
	s: int = 0
	for i in range(LIMIT):
		if is_palindrom(str(i)) and is_palindrom(dec_to_bin(i)):
			s += i

	print(f"{LIMIT} kisebb decimalis es binaris alakban palindrom szamok osszege: {s}")

if __name__ == "__main__":
	main()