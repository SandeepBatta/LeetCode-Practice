# # Challenge Context
# A company has n employees with a unique ID for each employee from 0 to n - 1. The head of the company is the one with headID.
# Each employee has one direct manager given in the manager array where manager[i] is the direct manager of the i-th employee, manager[headID] = -1. Also, it is guaranteed that the subordination relationships have a tree structure.
# The head of the company wants to inform all the company employees of an urgent piece of news. He will inform his direct subordinates, and they will inform their subordinates, and so on until all employees know about the urgent news.
# The i-th employee needs informTime[i] minutes to inform all of his direct subordinates (i.e., After informTime[i] minutes, all his direct subordinates can start spreading the news).
# Return the number of minutes needed to inform all the employees about the urgent news.

# Challenge Link --> https://leetcode.com/problems/time-needed-to-inform-all-employees/


class Solution:
    def numOfMinutes(
        self, n: int, headID: int, manager: list[int], informTime: list[int]
    ) -> int:
        subordinates = [[] for _ in range(n)]
        time_all_emp = 0
        for idx, m in enumerate(manager):
            if m != -1:
                subordinates[m].append(idx)

        visited = set([headID])
        queue = [(headID, 0)]
        while queue:
            emp = queue.pop(0)
            emp_idx = emp[0]
            if subordinates[emp_idx]:
                for i in subordinates[emp_idx]:
                    visited.add(i)
                    time = emp[1] + informTime[emp_idx]
                    queue.append((i, time))
            else:
                time_all_emp = max(time_all_emp, emp[1])

        return time_all_emp


Solution().numOfMinutes(6, 2, [2, 2, -1, 2, 2, 2], [0, 0, 1, 0, 0, 0])
