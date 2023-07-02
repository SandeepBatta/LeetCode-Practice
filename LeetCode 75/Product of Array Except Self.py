# # Problem Statement
# Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].
# The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
# You must write an algorithm that runs in O(n) time and without using the division operation.


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = 1
        output = [1]
        for num in nums[:-1]:
            prefix = prefix * num
            output.append(prefix)

        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            output[i] = output[i] * postfix
            postfix = postfix * nums[i]

        return output
