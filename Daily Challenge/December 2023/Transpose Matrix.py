# # Challenge Context
# Given a 2D integer array matrix, return the transpose of matrix.
# Challenge Link --> https://leetcode.com/problems/transpose-matrix/?envType=daily-question&envId=2023-12-10


class Solution:
    def transpose(self, matrix: list[list[int]]) -> list[list[int]]:
        output = [[] for _ in range(len(matrix[0]))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                output[j].append(matrix[i][j])
        return output
