#!/bin/python3

import re

# Read input dimensions
first_multiple_input = input().rstrip().split()
n = int(first_multiple_input[0])
m = int(first_multiple_input[1])

# Read the matrix rows
matrix = []
for _ in range(n):
    matrix_item = input()
    matrix.append(matrix_item)

# Initialize a list to collect characters from each column
decoded_string = []

# Process each column
for col in range(m):
    # Collect characters from the current column
    column_chars = ''.join(matrix[row][col] for row in range(n))
    decoded_string.append(column_chars)

# Join all column strings into one single string
decoded_string = ''.join(decoded_string)

# Replace sequences of non-alphanumeric characters between alphanumeric characters with a single space
# This regex pattern finds sequences of non-alphanumeric characters that are not at the start or end
decoded_string = re.sub(r'(?<=\w)[^\w]+(?=\w)', ' ', decoded_string)

# Print the final decoded string
print(decoded_string)
