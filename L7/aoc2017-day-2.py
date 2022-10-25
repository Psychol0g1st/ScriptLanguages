#!/usr/bin/env python3
#encoding: utf-8

def calculate_checksum(matrix):
    differences = []
    for row in matrix:
        min_num = min(row)
        max_num = max(row)
        differences.append(abs(min_num - max_num))
    return sum(differences)
def get_matrix_from_file(filename):
    matrix = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            digits = line.split()
            matrix.append([int(digit) for digit in digits])
    return matrix

def main():
    matrix = get_matrix_from_file('input.txt')
    print(calculate_checksum(matrix))

if(__name__ == "__main__"):
    main()