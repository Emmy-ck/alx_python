#!/usr/bin/python3

def square_matrix_simple(matrix=[]):
    new_matrix = [] #Creating an empty matrix to store squared values
    
    for row in matrix: #iterate through rown in the matrix
        new_row = [] #Create new empty row for the squared values
        
        for i in row: #Iterate through each element in the row and column
            squared_i = i ** 2
            new_row.append(squared_i)
            
        new_matrix.append(new_row) #Append the squared row to the new matrix
        
    return new_matrix