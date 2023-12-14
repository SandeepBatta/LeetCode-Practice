# # Challenge Context
# You are given a 0-indexed m x n binary matrix grid.
# Return the difference matrix diff.
# Challenge Link --> https://leetcode.com/problems/difference-between-ones-and-zeros-in-row-and-column/?envType=daily-question&envId=2023-12-14

from collections import defaultdict


class Solution:
    def onesMinusZeros(self, grid: list[list[int]]) -> list[list[int]]:
        row_ones = defaultdict(int)
        row_zeros = defaultdict(int)
        col_ones = defaultdict(int)
        col_zeros = defaultdict(int)

        for idx1, row in enumerate(grid):
            for idx2, col in enumerate(row):
                if col == 1:
                    row_ones[idx1] += 1
                elif col == 0:
                    row_zeros[idx1] += 1

        for col in range(len(grid[0])):
            for row in range(len(grid)):
                if grid[row][col] == 1:
                    col_ones[col] += 1
                elif grid[row][col] == 0:
                    col_zeros[col] += 1

        for idx1, row in enumerate(grid):
            for idx2, col in enumerate(row):
                grid[idx1][idx2] = (
                    row_ones[idx1] + col_ones[idx2] - row_zeros[idx1] - col_zeros[idx2]
                )
        return grid
