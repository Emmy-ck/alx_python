#!/usr/bin/python3

# def print_matrix_integer(matrix=[[]]):
#     for row in matrix:
#         for i in range(0, len(row)):
#             if i == len(row) - 1:
#                 print("{:d}".format(row[i]))
#             else:
#                 print("{:d}".format(row[i]), end=" ")
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in range(len(row)):
            print("{:d}".format(row[i]), end="")
            if i != len(row) - 1:
                print(" ", end="")
        print()