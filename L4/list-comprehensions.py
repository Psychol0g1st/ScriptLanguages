#!/usr/bin/env python3
# encoding: utf-8
def task_print(num, r, l=None):
    if not l == None:
        print(str(num) + ".", l, "->", r)
    else:
        print(str(num) + ".", r)
    print("-"*10, "\n")

def main():
    l1 = ['auto', 'villamos', 'metro']
    r1 = [s.upper() + "!" for s in l1]
    task_print(1, r1, l1)
    l2 = ['aladar', 'bela', 'cecil']
    r2 = [name.capitalize() for name in l2]
    task_print(2, r1, l2)
    r3 = [0 for i in range(10)]
    task_print(3, r3)
    # l4 = list(range(1, 11))
    r4 = [num*2 for num in range(1, 11)]
    task_print(4, r4)
    l5 = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    r5 = [int(s) for s in l5]
    task_print(5, r5, l5)
    l6 = "1234567"
    r6 = [int(s) for s in l6]
    task_print(6, r6, l6)
    l7 = "The quick brown fox jumps over the lazy dog"
    r7 = [len(word) for word in l7.split()]
    task_print(7, r7, l7)
    l8 = "python is an awesome language"
    r8 = [word[0] for word in l8.split()]
    task_print(8, r8, l8)
    l9 = "The quick brown fox jumps over the lazy dog"
    r9 = [(word, len(word)) for word in l9.split()]
    task_print(9, r9, l9)
    r10 = [i for i in range(0,10, 2)]
    task_print(10, r10)
    r11 = [i**2 for i in range(20) if (i**2) % 2 == 0]
    task_print(11, r11)
    r12 = [i**2 for i in range(20) if (i**2) % 10 == 4]
    task_print(12, r12)
    r13 = [chr(char) for char in range(65, 91)]
    task_print(13, r13)
    l14 = [' apple ', ' banana ', ' kiwi']
    r14 = [word.strip() for word in l14]
    task_print(14, r14, l14)
    l15 = [1, 0, 1, 1, 0, 1, 0, 0]
    r15 = "".join([str(num) for num in l15])
    task_print(15, r15, l15)

if(__name__ == "__main__"):
    main()