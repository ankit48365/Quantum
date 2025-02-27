
# Input values
# matrix_values = [0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5]
matrix_values = [2,-1,9,4]
columns_per_row = 2


import numpy as np
from sympy import Matrix

# Function to convert array to matrix
def array_to_matrix(array, cols):
    rows = len(array) // cols
    return np.array(array).reshape(rows, cols)

# Function to convert matrix to Dirac notation
def matrix_to_dirac(matrix, decimals=2):
    sympy_matrix = Matrix(matrix)
    rows, cols = sympy_matrix.shape
    dirac_notation = ""
    for i in range(rows):
        for j in range(cols):
            if sympy_matrix[i, j] != 0:
                # Round the element to the specified number of decimal places
                element = round(float(sympy_matrix[i, j]), decimals)
                dirac_notation += f"{element}|{i}><{j}| + "
    return dirac_notation[:-3]  # Remove the trailing ' + '



# Convert array to matrix
matrix = array_to_matrix(matrix_values, columns_per_row)

# Print the Dirac notation
dirac_notation = matrix_to_dirac(matrix)
print(dirac_notation)
