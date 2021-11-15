# Taken from lectures in weeks 5-6

"""
input:
knapsack_weight: int. The weight that the knapsack can hold.
items: list[tuple[int, int]]. List of pairs (tuples) that represent items.
each item have value and weight. the value is the first cel in the tuple and the weight is the second.

output:
list[int], represents the indexes of the items that will bring the maximum value while the total weight is under the
weight of knapsack_weight
"""

from renderer_tables import *

def knapsack_problem_helper(current_weight: int, item_value: int, item_weight: int, coordinates: tuple[int, int], table: list[list[int]]):
    if item_weight > current_weight:
        # put the last cell in the current cell - so we don't insert new item
        table[coordinates[0]].append(table[coordinates[0]+1][coordinates[1]])
    else:
        # check what is better - with this item or without - and insert the best choice
        without_current_item = table[coordinates[0]+1][coordinates[1]]
        with_current_item = table[coordinates[0]+1][coordinates[1]-item_weight+1] + item_value
        table[coordinates[0]].append(max(without_current_item, with_current_item))


def knapsack_problem(knapsack_weight: int, items: list[tuple[int, int]]):
    # init table with n lists (rows)
    table = list()
    for k in range(len(items)):
        table.append(list())
    for i in range(len(items)-1, -1, -1):  # every i is an item
        for j in range(knapsack_weight):  # every j is a weight
            # init last row to be 0
            if i == len(items)-1:
                if items[i][1] > j:
                    table[i].append(0)
                    continue
                else:
                    table[i].append(items[i][0])
                    continue
            # check the step of the recursion, after that the table(i,j) should be filled
            knapsack_problem_helper(j, items[i][0], items[i][1], (i, j), table)
    print_table(table)
    return table[0][knapsack_weight - 1]

def knapsack_problem_test():
    knapsack_problem(50, [(150, 30), (100, 25), (100, 25)])

knapsack_problem_test()
