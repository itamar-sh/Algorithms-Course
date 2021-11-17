# Inspired by lecture in week 5
# Written by Itamar Shechter

"""
problem description:
We want to find the minimal number of operations to find the multiplying of series of matrices
example: we have matrices, A, B ,C, D, E
we want to know in which order we should multiply them.
Different order will give the same matrix but not in the same amount of operations to get the matrix.
"""
import math
from renderer_tables import *

def minimal_matrices_multiplication(matrices_list: list[int]) ->int:
    """
    We build a table. Every cell in the table will represents the num of operations that required to calculate
    subset of the main problem.
    table[i][j] will hold the num of operations to calculate A_i*...*A_j matrices
    So the solution will be in table[1][n]

    :param matrices_list: list of ints that represents the num of rows and cols of each pair of matrices
    :return: num of minimal operations to find the multiplied matrix
    """
    num_of_matrices = len(matrices_list)-1
    table = list()
    for i in range(num_of_matrices):
        table.append([0]*num_of_matrices)
    # we want to fill the table by go over each diagonal from the main diagonal
    diagonal_number = 1
    for i in range(num_of_matrices):
        cells_in_diagonal = go_over_diagonal(table, i, 0, 1, 1)
        for tuple_of_indexes in cells_in_diagonal:
            row, col = tuple_of_indexes
            table[row][col] = calculate_cell(row, col, table, matrices_list)
    print_table(table)
    return table[num_of_matrices-1][0]

def calculate_cell(row: int, col: int, table: list[list[int]], matrices_list):
    if row == col:
        return 0
    min_value = math.prod(matrices_list)
    d = row - col + 1
    for k in range(1, d):
        up_cell = table[row - k + 1][col]
        right_cell = table[row][col + k]
        current_operations = matrices_list[col]*matrices_list[col + k]*matrices_list[row + 1]
        sum_operations = up_cell + right_cell + current_operations
        min_value = min(min_value, sum_operations)
    return min_value

def go_over_diagonal(table: list[list[int]], row: int, col: int, row_delta: int, col_delta: int) -> list[tuple[int, int]]:
    rows = len(table)
    cols = len(table[0])
    result = list()
    while rows > row >= 0 and cols > col >= 0:
        result.append((row, col))
        row += row_delta
        col += col_delta
    return result

def minimal_matrices_multiplication_test():
    # assert 10000 == minimal_matrices_multiplication([10, 50, 20])
    print(minimal_matrices_multiplication([10, 50, 20, 100]))

minimal_matrices_multiplication_test()