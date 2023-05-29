# # Problem Statement
# You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.
# Return the merged string.


class Solution:
    def mergealternately(self, word1: str, word2: str) -> str:
        output = ""
        if len(word1) >= len(word2):
            for idx in range(len(word2)):
                output = output + word1[idx] + word2[idx]
            output = output if len(word1) == len(word2) else output + word1[idx + 1 :]
        else:
            for idx in range(len(word1)):
                output = output + word1[idx] + word2[idx]
            output = output + word2[idx + 1 :]
        return output
