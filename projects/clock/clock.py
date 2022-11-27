#!/usr/bin/env python3
# encoding: utf-8

import os
from datetime import datetime
import sys

DIGITS = [
	[" ┏━┓ ", "  ╻  ", " ┏━┓ ", " ┏━┓ ", " ╻ ╻ ", " ┏━┓ ", " ┏   ", " ┏━┓ ", " ┏━┓ ", " ┏━┓ ", "   "],
	[" ┃ ┃ ", "  ┃  ", "   ┃ ", "   ┃ ", " ┃ ┃ ", " ┃   ", " ┃   ", "   ┃ ", " ┃ ┃ ", " ┃ ┃ ", " ╻ "],
	[" ┃ ┃ ", "  ┃  ", "   ┃ ", "   ┃ ", " ┃ ┃ ", " ┃   ", " ┃   ", "   ┃ ", " ┃ ┃ ", " ┃ ┃ ", "   "],
	[" ┃ ┃ ", "  ┃  ", " ┏━┛ ", " ┣━┫ ", " ┗━┫ ", " ┗━┓ ", " ┣━┓ ", "   ┃ ", " ┣━┫ ", " ┗━┫ ", "   "],
	[" ┃ ┃ ", "  ┃  ", " ┃   ", "   ┃ ", "   ┃ ", "   ┃ ", " ┃ ┃ ", "   ┃ ", " ┃ ┃ ", "   ┃ ", "   "],
	[" ┃ ┃ ", "  ┃  ", " ┃   ", "   ┃ ", "   ┃ ", "   ┃ ", " ┃ ┃ ", "   ┃ ", " ┃ ┃ ", "   ┃ ", " ╹ "],
	[" ┗━┛ ", "  ╹  ", " ┗━━ ", " ┗━┛ ", "   ╹ ", " ┗━┛ ", " ┗━┛ ", "   ╹ ", " ┗━┛ ", " ┗━┛ ", "   "],
]
SYMBOLS = {
    "0" : 0,
    "1" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    ':' : 10,
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_clock(time_str):
    clear_screen()
    sb = []
    for row in DIGITS:
        for s in time_str:
            sb.append(row[SYMBOLS[s]])
        sb.append('\n')
    print("".join(sb))



def hide_cursor():
    sys.stdout.write("\033[?25l")
    sys.stdout.flush() 



def main():
    hide_cursor()
    old_time_str = ""
    while(True):
        time_str = datetime.now().strftime("%H:%M:%S")
        if time_str != old_time_str:
            print_clock(time_str)
            old_time_str = time_str


if(__name__ == "__main__"):
    main()