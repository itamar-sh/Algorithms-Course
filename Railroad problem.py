# Taken from practice 5
# This is an NP problem so we dont know a better solution for this.

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


def rail_road(rail_len: int, connectors: int, parts: list[list[int]]) -> int:
    return 1
