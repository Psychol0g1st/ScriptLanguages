#!/usr/bin/env python3
# encoding: utf-8

import os
import json

PATH = "data/"


def main():

    files = os.listdir("./data")
    songs_duration = []
    for filename in files:
        with open(PATH + filename, "r") as file:
            s = file.read()
            songs_duration.append(json.loads(s)["data"]["duration"])
    average_duration = sum(songs_duration) / len(songs_duration)
    print("A számok átlagos hossza {:.1f} másodperc.".format(average_duration))


if __name__ == "__main__":
    main()
