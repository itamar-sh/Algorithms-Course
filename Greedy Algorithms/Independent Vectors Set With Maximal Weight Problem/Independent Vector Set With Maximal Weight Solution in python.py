from typing import List, Callable

import numpy as np
import sympy as sympy

Vector = np.array  # alternative option is list[float]

class Independent_Vectors_Set_With_Maximal_Weight_Solution:
    def main_solution(self, vectors: List[Vector], weight_func: Callable[[Vector], int]) -> List[Vector]:
        # check for invalidity question
        if len(vectors) == 0:
            return []
        len_of_vector = len(vectors[0])
        for vector in vectors:
            if len(vector) != len_of_vector:
                return []
        # solution:
        vectors.sort(key=lambda v : weight_func(v), reverse=True)
        # solution_list = np.zeros((len(vector), len(vector)))
        # solution_list[0] = vectors.pop(0)
        solution_list = [vectors.pop(0)]
        index = 1
        while len(vectors) != 0:
            # remove all the dependents vectors
            remove_list = []
            for vector in vectors: # find dependent vectors
                temp_solution_list = solution_list[:]
                temp_solution_list.append(vector)
                temp_solution_list = np.array(temp_solution_list)
                _, indexes = sympy.Matrix(temp_solution_list).T.rref()
                if len(solution_list) not in indexes:
                    remove_list.append(vector)
            # remove them
            for vector in remove_list:
                vectors.remove(vector)
            # add new vector
            solution_list.append(vectors.pop(0))
        return solution_list

def weight_func_test(vector: Vector):
    sum = 0
    for i in range(len(vector)):
        sum += i*vector[i]
    return sum
if __name__ == '__main__':

    solver = Independent_Vectors_Set_With_Maximal_Weight_Solution()
    assert(solver.main_solution([[0,0,0,1],[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]], weight_func_test) ==
           [[0, 0, 0, 1], [0, 0, 1, 0], [0, 1,0, 0], [1, 0, 0, 0]])

