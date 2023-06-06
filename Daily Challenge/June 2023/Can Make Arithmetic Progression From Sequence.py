# # Challenge Context
# A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.
# Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.
# Challenge Link --> https://leetcode.com/problems/can-make-arithmetic-progression-from-sequence/


class Solution:
    def canMakeArithmeticProgression(self, arr: list[int]) -> bool:
        arr.sort()
        diff = arr[1] - arr[0]
        for i in range(1, len(arr) - 1):
            if arr[i + 1] - arr[i] != diff:
                return False
        return True
