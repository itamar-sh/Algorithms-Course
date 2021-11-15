def print_table(table: list[list[int]]):
    print(" | " + " - "*len(table[0]) + " | ")
    for i in range(len(table)):
        print(" | ", end="")
        for j in range(len(table[i])):
            print(table[i][j], end=" ")
        print(" | ")
    print(" | " + " - " * len(table[0]) + " | ")
