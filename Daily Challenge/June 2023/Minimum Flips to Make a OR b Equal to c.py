# # Challenge Context
# Given 3 positives numbers a, b and c. Return the minimum flips required in some bits of a and b to make ( a OR b == c ). (bitwise OR operation).
# Flip operation consists of change any single bit 1 to 0 or change the bit 0 to 1 in their binary representation.

# Challenge Link --> https://leetcode.com/problems/minimum-flips-to-make-a-or-b-equal-to-c/


class Solution:
    def dec_to_binary(self, decnum: int) -> str:
        return bin(decnum)[2:]

    def leading_zeros(self, bin: str, max_len: int) -> str:
        no_zeroes = max_len - len(bin)
        return "0" * no_zeroes + bin

    def minFlips(self, a: int, b: int, c: int) -> int:
        a = self.dec_to_binary(a)
        b = self.dec_to_binary(b)
        c = self.dec_to_binary(c)

        max_len = max(len(a), len(b), len(c))
        a = self.leading_zeros(a, max_len)
        b = self.leading_zeros(b, max_len)
        c = self.leading_zeros(c, max_len)

        flips = 0
        for idx, i in enumerate(c):
            if i == "0":
                flips = flips + 1 if a[idx] == "1" else flips
                flips = flips + 1 if b[idx] == "1" else flips
            if i == "1":
                flips = flips + 1 if a[idx] == "0" and b[idx] == "0" else flips
        return flips
