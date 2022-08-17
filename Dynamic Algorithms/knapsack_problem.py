# Inspired by lecture in week 5
# Written by Itamar Shechter

"""
input:
knapsack_weight: int. The weight that the knapsack can hold.
items: list[tuple[int, int]]. List of pairs (tuples) that represent items.
each item have value and weight. the value is the first cel in the tuple and the weight is the second.

output:
list[int], represents the indexes of the items that will bring the maximum value while the total weight is under the
weight of knapsack_weight
"""

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
    # init last row. last row == len(items)-1
    for j in range(knapsack_weight):  # every j is a weight
        if items[len(items)-1][1] > j:
            table[len(items)-1].append(0)
            continue
        else:
            table[len(items)-1].append(items[len(items)-1][0])
            continue
    # fill the rest of the table
    for i in range(len(items)-2, -1, -1):  # every i is an item, we already passed the last row
        for j in range(knapsack_weight):  # every j is a weight
            # check the step of the recursion, after that the table(i,j) should be filled
            knapsack_problem_helper(j, items[i][0], items[i][1], (i, j), table)
    # uncomment if you want to print the table
    # print_table(table)
    return table[0][knapsack_weight - 1]

def knapsack_problem_test():
    assert 200 == knapsack_problem(50, [(150, 30), (100, 25), (100, 25)])


def print_table(table: list[list[int]]):
    print(" | " + " - "*len(table[0]) + " | ")
    for i in range(len(table)):
        print(" | ", end="")
        for j in range(len(table[i])):
            print(table[i][j], end=" ")
        print(" | ")
    print(" | " + " - " * len(table[0]) + " | ")

if __name__ == '__main__':
    knapsack_problem_test()


