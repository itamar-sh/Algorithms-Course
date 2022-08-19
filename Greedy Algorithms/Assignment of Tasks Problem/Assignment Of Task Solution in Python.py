from typing import List, Tuple

class Tasks_assignments:  # O(n*log(n))
    def tasks_assignments_solution(self, start_list: List[int], finish_list: List[int]) -> List[int]:
        if len(start_list) != len(finish_list):  # O(1)
            return []
        tasks_list = self.make_tasks_list(start_list, finish_list)  # O(n)
        self.sort_by_finish_list(tasks_list)  # O(n*log(n))
        index = 1
        result_list = [0]
        while index < len(tasks_list):  # O(n)
            if tasks_list[index][0] < tasks_list[result_list[-1]][1]:  # End of last task bigger than start of new task
                index += 1
            else:   # strangers to each other
                result_list.append(index)
        return result_list

    def sort_by_finish_list(self, tasks_list: List[Tuple[int,int]]) -> None:
        def key_func(task: Tuple[int, int]):
            return task[1]

        tasks_list.sort(reverse=False, key=key_func)

    def make_tasks_list(self, start_list: List[int], finish_list: List[int]) -> List[Tuple[int, int]]:
        tasks_list = []
        for i in range(len(start_list)):
            tasks_list.append((start_list[i], finish_list[i]))
        return tasks_list


if __name__ == '__main__':
    solver = Tasks_assignments()
    assert(solver.tasks_assignments_solution([0,1,2], [2,3,4]) == [0,2])
    assert(solver.tasks_assignments_solution([0,5,2], [2,6,4]) == [0,1,2])
    assert(solver.tasks_assignments_solution([2,1,0], [4,3,2]) == [0,2])
