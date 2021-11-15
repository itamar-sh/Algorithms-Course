class Matrix:
    """ Matrix of int, represents with list of lists with the same lengths. Similar to table.

    Attributes:
        rows: number of lines.
        cols: length of every line in the matrix
        lines: list of lines (lists).
    """
    rows: int
    cols: int
    lines: list[list[int]]

    def __init__(self, lines: list[list[int]]):
        """Initializes a `Proof` from its assumptions/axioms, conclusion,
        and lines.

        Parameters:
            lines: list of lines (lists).
        """
        self.rows = len(list)
        self.cols = len(list[0])
        for i in range(self.rows):
            self.lines.append(list())
            for j in range(self.cols):
                self.lines[i].append(lines[i][j])

    @staticmethod
    def go_over_diagonal(matrix: list[list[int]], row: int, col: int, row_delta: int, col_delta: int) -> list[tuple[int, int]]:
        rows = len(list)
        cols = len(list[0])
        result = list()
        while rows > row >= 0 and cols > col >= 0:
            result.append((row, col))
            row += row_delta
            col += col_delta
        return result


