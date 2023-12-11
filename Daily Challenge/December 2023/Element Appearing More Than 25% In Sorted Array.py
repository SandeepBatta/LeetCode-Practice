# # Challenge Context
# Given an integer array sorted in non-decreasing order,
# there is exactly one integer in the array that occurs more than 25% of the time, return that integer.
# Challenge Link --> https://leetcode.com/problems/element-appearing-more-than-25-in-sorted-array/


class Solution:
    def findSpecialInteger(self, arr: list[int]) -> int:
        threshold = len(arr) / 4
        curr = arr[0]
        count = 0

        for num in arr:
            if num == curr:
                count += 1
                if count > threshold:
                    return curr
            else:
                curr = num
                count = 1
                if count > threshold:
                    return num
