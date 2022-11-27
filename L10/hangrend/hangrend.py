from typing import Tuple

MELY_MGHK: str = 'aáoóuú'
MAGAS_MGHK: str = 'eéiíöőüű'
HANGREND_TIPUSOK: Tuple[str, str, str, str] = ('semmilyen', "mely", "magas", "vegyes")

def hangrend(word: str) -> str:
    magas: int = 0
    mely: int = 0
    for letter in word:
        if letter in MELY_MGHK:
            mely = 1
        elif letter in MAGAS_MGHK:
            magas = 2
    return HANGREND_TIPUSOK[mely + magas]


def main() -> None:
    words: list[str] = ["ablak", "erkély", "kisvasút", "magas", "mély", "pfff"]
    for word in words:
        print(word, "->", hangrend(word))
#############################################################################

if __name__ == "__main__":
    main() 