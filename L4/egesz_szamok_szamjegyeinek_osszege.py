#!/usr/bin/env python3


from multiprocessing.dummy import Array
import string
from unittest import result


def main():
    str_num_list = [list(str(num)) for num in range(1,101)]
    result = 0
    for nums in str_num_list:
        for digit in nums:
            result += int(digit)
    print("1-100 egesz szamok szamjegyinek osszege:", result)

#############################################################################

if __name__ == "__main__":
    main()