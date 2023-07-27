#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in row:
            print("{:d}".format(i), end=" ")
        print()
            # if i == len(row) - 1:
            #     print("{:d}".format(row[i]))
            # else:
            #     print("{:d}".format(row[i]), end=" ")
