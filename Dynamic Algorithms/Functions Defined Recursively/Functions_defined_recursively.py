class FunctionsDefinedRecursively:
    def solve(self, a: int, b: int):
        if a == 0 or b == 0:
            return 1
        mat = []
        for i in range(a+1):
            mat.append([])
            for j in range(b+1):
                if i == 0 or j == 0:
                    mat[i].append(1)
                else:
                    mat[i].append(mat[i-1][j] + mat[i][j-1])
        return mat[-1][-1]

if __name__ == '__main__':
    solver = FunctionsDefinedRecursively()
    assert(solver.solve(1, 0) == 1)
    assert(solver.solve(1, 1) == 2)
    assert(solver.solve(2, 1) == 3)
    assert(solver.solve(2, 2) == 6)
    assert(solver.solve(3, 1) == 4)
    assert(solver.solve(3, 2) == 10)
    assert(solver.solve(3, 3) == 20)
