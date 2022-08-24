from typing import List


class TaskRoutingProblem:
    def solve(self, X: List[int], A: List[int], Y: List[int], B: List[int]):
        if len(X) != len(A)+2 or len(Y) != len(B)+2:
            return -1
        P_u = list()
        P_u.append(X[0])
        P_d = list()
        P_d.append(Y[0])
        for i in range(0, len(A)):
            P_u.append(min(X[i+1]+P_u[i-1], A[i]+P_d[i-1]))
            P_d.append(min(Y[i+1]+P_d[i-1], B[i]+P_u[i-1]))
        return min(P_d[-1] + Y[-1], P_u[-1] + X[-1])


if __name__ == '__main__':
    solver = TaskRoutingProblem()
    X = [2, 9, 1]
    Y = [3, 8, 1]
    A = [1]
    B = [10]
    assert 5 == solver.solve(X, A, Y, B)
    # We want to move like that: X[0] -> A[0] -> Y[2]
    # its equal to qo:      s->   U1  ->  D1  -> f
