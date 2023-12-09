# # Challenge Context
# You are given an integer n
# Return the number of matches played in the tournament until a winner is decided.
# Challenge Link --> https://leetcode.com/problems/count-of-matches-in-tournament/?envType=daily-question&envId=2023-12-05


class Solution:
    def numberOfMatches(self, n: int, matches=0) -> int:
        if n == 1:
            return matches
        elif n % 2 == 0:
            matches = self.numberOfMatches(n / 2, matches + n / 2)
        else:
            matches = self.numberOfMatches((n - 1) / 2 + 1, matches + (n - 1) / 2)
        return int(matches)
