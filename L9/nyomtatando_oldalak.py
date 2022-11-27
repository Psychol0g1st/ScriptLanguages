
def process_interval(interval: str) -> set[int]:	
	separated_values = [int(value.strip()) for value in interval.split("-")]
	begin: int
	end: int 
	begin,end = tuple(separated_values)
	
	if begin > end:
		begin,end = end,begin

	return set(range(begin, end+1))

def printable_pages(input_pages: str) -> list[int]:
	
	pages_set: set[int] = set()
	separated_input: list[str] = input_pages.split(",")
	for value in separated_input:
		value = value.strip()
		if len(value) > 0:
			if("-" in value):
				pages_set.update(process_interval(value))
			else:
				pages_set.add(int(value))
		
		ordered_pages: list[int] = sorted(list(pages_set))
	
	return ordered_pages

def printable_pages_to_str(pages: list[int]) -> str:
	if(len(pages) == 0):
		return "Nincs nyomtatando oldal"
	return f"Nyomtatando oldalak: {str(pages)[1:-1]}"

def main() -> None:
	print("""
A nyomtatando oldalakat vessovel kell elvalasztani.
Ket fele erteket meg lehet adni:
	1. Konkret oldal szam
	2. Oldal intervallumot ('-' elvalaszto jel segitsegevel)
Pelda: 1,2,3-10,25
	""")

	input_pages: str = input("Add meg a nyomtatando oldalakat\n:")
	
	pages: list[int] = printable_pages(input_pages)

	print(printable_pages_to_str(pages))

if __name__ == "__main__":
	main()