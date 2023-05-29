# # Problem Statement
# You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).
# Find two lines that together with the x-axis form a container, such that the container contains the most water.
# Return the maximum amount of water a container can store.

# # Solution 1
# class Solution:
#     def maxArea(self, height: list[int]) -> int:
#         maxarea = 0
#         for idx1 in range(len(height) - 1):
#             for idx2 in range(idx1, len(height)):
#                 area = (idx2 - idx1) * min(height[idx1], height[idx2])
#                 maxarea = max(area, maxarea)
#         return maxarea


# Solution 2
class Solution:
    def maxArea(self, height: list[int]) -> int:
        maxarea = 0
        l_pointer = 0
        r_pointer = len(height) - 1
        while True:
            if l_pointer == r_pointer:
                return maxarea
            area = (r_pointer - l_pointer) * min(height[l_pointer], height[r_pointer])
            maxarea = max(area, maxarea)
            if height[l_pointer] > height[r_pointer]:
                r_pointer -= 1
            else:
                l_pointer += 1
