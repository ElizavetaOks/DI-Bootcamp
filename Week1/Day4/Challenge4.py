matrix = """
7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!
"""
# To decrypt the matrix, Neo reads each column from top to bottom, starting from the leftmost column, 
# selecting only the alpha characters and connecting them. 
# Then he replaces every group of symbols between two alpha characters by a space.
# Using his technique, try to decode this matrix.

matrix_lines = matrix.strip().split('\n')
# print(matrix_lines)
transposed_matrix = list(map(list, zip(*matrix_lines)))
# print(transposed_matrix)
decoded_columns = [''.join([char for char in column if char.isalpha()]) for column in transposed_matrix]
# print(decoded_columns)
decoded_text = ' '.join(decoded_columns)

print(decoded_text)
