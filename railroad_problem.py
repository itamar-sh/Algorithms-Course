# Taken from practice 5
# This is an NP problem so we dont know a good solution for this.

"""
Input:
rail_len: int. represents the length of the rail.
connectors: int. All the kinds of connectors. each kind of connector represented by a number.
parts : list[list[int]]. Every part is a list of 4 int.
The first int is the kind of connector in the beginning.
The second int is the kind of connector in the end.
the third int is the length of the current part.
the fourth int is the cost of the current part.

Output:
int: the cost of legal rail in length of rail_len.
Legal rail is a rail that all the linked parts are connected with the same connectors.
"""


# naive solution - will take a lot of time with big input
def rail_road(rail_len: int, connectors: int, parts: list[list[int]], last_connection = -1) -> int:
    # base of recursion
    if rail_len == 0:
        return 0
    # step
    min_cost = 0
    part_chosen = False
    for i in range(connectors):
        if (parts[i][1] == last_connection or last_connection == -1) and rail_len - parts[i][2] >= 0:
            next_value = rail_road(rail_len - parts[i][2], connectors, parts, parts[i][0])
            if next_value == -1:
                continue
            min_cost = min(min_cost, next_value)
            part_chosen = True
    if part_chosen:
        return -1
    return min_cost

