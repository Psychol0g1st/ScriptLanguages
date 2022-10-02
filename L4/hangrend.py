#!/usr/bin/env python3

MELY_MGHK = 'aáoóuú'
MAGAS_MGHK = 'eéiíöőüű'
HANGREND_TIPUSOK = ('semmilyen', "mely", "magas", "vegyes")

def hangrend(word):
    magas = 0
    mely = 0
    for letter in word:
        if letter in MELY_MGHK:
            mely = 1
        elif letter in MAGAS_MGHK:
            magas = 2
    return HANGREND_TIPUSOK[mely + magas]


def main():
    words = ["ablak", "erkély", "kisvasút", "magas", "mély", "pfff"]
    for word in words:
        print(word, "->", hangrend(word))
#############################################################################

if __name__ == "__main__":
    main()