#!/usr/bin/env python3
from enum import Enum

class Hangrend(Enum):
    SEMMILYEN = 'semmilyen'
    MELY = 'mely'
    MAGAS = 'magas'
    VEGYES = 'vegyes'

MELY_MGHK = 'aáoóuú'
MAGAS_MGHK = 'eéiíöőüű'

def hangrend(word):
    magas = 0
    mely = 0
    for letter in word:
        if letter in MELY_MGHK:
            mely = 1
        elif letter in MAGAS_MGHK:
            magas = 2
    if magas + mely == 1:
        return Hangrend.MELY.value
    elif magas + mely == 2:
        return Hangrend.MAGAS.value
    elif magas + mely == 3:
        return Hangrend.VEGYES.value
    else:
        return Hangrend.SEMMILYEN.value

def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "pfff"]
    for word in words:
        print(word, "->", hangrend(word))
#############################################################################

if __name__ == "__main__":
    main()