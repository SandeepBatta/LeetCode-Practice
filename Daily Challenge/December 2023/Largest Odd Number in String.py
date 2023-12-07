# # Challenge Context
# You are given a string num, representing a large integer.
# Return the largest-valued odd integer (as a string) that is a non-empty substring of num, or an empty string "" if no odd integer exists.
# Challenge Link --> https://leetcode.com/problems/largest-odd-number-in-string/?envType=daily-question&envId=2023-12-07


class Solution:
    def largestOddNumber(self, num: str) -> str:
        output = num
        for n in num[-1::-1]:
            if int(n) % 2 != 0:
                return output
            else:
                output = output[:-1]
        return output