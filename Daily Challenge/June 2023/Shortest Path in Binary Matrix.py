# # Challenge Context
# Given an n x n binary matrix grid, return the length of the shortest clear path in the matrix. If there is no clear path, return -1.

# Challenge Link --> https://leetcode.com/problems/shortest-path-in-binary-matrix/


class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        rows, cols = len(grid), len(grid[0])

        # Return if top-left or bottom-right cells are not zero
        if grid[0][0] == 1 or grid[rows - 1][cols - 1] == 1:
            return -1

        # BFS algorithm
        queue = [(0, 0, 1)]
        grid[0][0] = 1

        while queue:
            r, c, d = queue.pop(0)

            # Return the distance as soon as we reach the bottom-right cell
            if (r, c) == (rows - 1, cols - 1):
                return d

            # 8 possible neighbour cells
            directions = [
                (r + 1, c),
                (r, c + 1),
                (r - 1, c),
                (r, c - 1),
                (r + 1, c + 1),
                (r - 1, c - 1),
                (r + 1, c - 1),
                (r - 1, c + 1),
            ]

            for r, c in directions:
                if r in range(rows) and c in range(cols) and grid[r][c] == 0:
                    grid[r][c] = 1
                    queue.append((r, c, d + 1))

        return -1
