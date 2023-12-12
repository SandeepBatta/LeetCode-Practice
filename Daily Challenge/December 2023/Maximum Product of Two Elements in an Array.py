# # Challenge Context
# Given the array of integers nums, you will choose two different indices i and j of that array. Return the maximum value of (nums[i]-1)*(nums[j]-1).
# Challenge Link --> https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/?envType=daily-question&envId=2023-12-12


class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        if nums[0] > nums[1]:
            max1 = nums[0]
            max2 = nums[1]
        else:
            max1 = nums[1]
            max2 = nums[0]

        for num in nums[2:]:
            if num > max1:
                max1, max2 = num, max1
            elif num > max2:
                max2 = num
        return (max1 - 1) * (max2 - 1)
