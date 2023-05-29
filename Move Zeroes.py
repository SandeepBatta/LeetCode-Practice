# # Problem Statement
# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# Note that you must do this in-place without making a copy of the array.


class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Set the pointers to extreme ends
        l_pointer, r_pointer = 0, len(nums) - 1

        # Exit the loop when pointers meet
        while True:
            if l_pointer == r_pointer:
                break

            # Pop the '0' element and append it to the end
            if nums[l_pointer] == 0:
                nums.pop(l_pointer)
                nums.append(0)
                r_pointer -= 1
            else:
                l_pointer += 1
