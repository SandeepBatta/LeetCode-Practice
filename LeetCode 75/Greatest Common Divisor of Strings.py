# # Problem Statement
# For two strings s and t, we say "t divides s" if and only if s = t + ... + t (i.e., t is concatenated with itself one or more times).
# Given two strings str1 and str2, return the largest string x such that x divides both str1 and str2.


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        sub_str = str1 if min(len(str1), len(str2)) == len(str1) else str2

        while True:
            if sub_str == "":
                return ""

            if len(str1) % len(sub_str) == 0 and len(str2) % len(sub_str) == 0:
                if str1 == sub_str * int(
                    (len(str1) / len(sub_str))
                ) and str2 == sub_str * int((len(str2) / len(sub_str))):
                    return sub_str

            sub_str = sub_str[:-1]
