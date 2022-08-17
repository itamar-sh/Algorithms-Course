from typing import List, Tuple


class Fractional_knapcpack_problem:

    def Fractional_knapcpack_problem_solution(self, items: List[Tuple[int, int]], max_weight: int):
        items_with_specific_values = self.calculate_specific_value(items)
        self.sort_by_specific_value(items_with_specific_values)
        cur_sum_weight = 0
        cur_sum_value = 0
        index = 0
        while cur_sum_weight < max_weight:
            cur_item = items_with_specific_values[index]
            if cur_sum_weight + cur_item[2] < max_weight:
                cur_sum_weight += cur_item[2]
                cur_sum_value += cur_item[1]
            else:
                left_space = max_weight - cur_sum_weight
                cur_sum_weight = max_weight
                cur_sum_value += cur_item[1] * (left_space / cur_item[2])
            index += 1
        return cur_sum_value

    def calculate_specific_value(self, items: List[Tuple[int, int]]) -> List[Tuple[float, int, int]]:
        """
        Each item in the input is composed from value and weight.
        So item[0] is the value of the item
        and item[1] is the weight of the item.
        Args:
            items:

        Returns:

        """
        specific_values = []
        for item in items:
            specific_values.append((item[0]/item[1], item[0], item[1]))

        return specific_values

    def sort_by_specific_value(self, items_with_specific_values: List[Tuple[float, int, int]]):
        def check_specific_value(item):
            return item[0]

        items_with_specific_values.sort(reverse=True, key=check_specific_value)


if __name__ == '__main__':
    solver = Fractional_knapcpack_problem()
    assert(solver.Fractional_knapcpack_problem_solution([(100,100),(50,50),(25,50)], 150)==150)
    assert(solver.Fractional_knapcpack_problem_solution([(100,50),(50,50),(25,50)], 100)==150)
    assert(solver.Fractional_knapcpack_problem_solution([(100,50),(50,50),(25,50)], 125)==162.5)

