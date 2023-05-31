# # Problem Statement
# Given a string s, reverse only all the vowels in the string and return it.
# The vowels are 'a', 'e', 'i', 'o', and 'u', and they can appear in both lower and upper cases, more than once.


# Solution 1
# class Solution:
#     def reverseVowels(self, s: str) -> str:
#         l_pointer = 0
#         r_pointer = len(s) - 1
#         vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

#         output = s
#         while l_pointer < r_pointer:
#             if s[l_pointer] in vowels and s[r_pointer] in vowels:
#                 output = (
#                     output[:l_pointer]
#                     + output[r_pointer]
#                     + output[l_pointer + 1 : r_pointer]
#                     + output[l_pointer]
#                     + output[r_pointer + 1 :]
#                 )
#                 l_pointer += 1
#                 r_pointer -= 1
#             elif s[l_pointer] in vowels:
#                 r_pointer -= 1
#             elif s[r_pointer] in vowels:
#                 l_pointer += 1
#             else:
#                 l_pointer += 1
#                 r_pointer -= 1
#         return output


# Solution 2
class Solution:
    def reverseVowels(self, s: str) -> str:
        l_pointer = 0
        r_pointer = len(s) - 1
        vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

        output = list(s)
        while l_pointer < r_pointer:
            if s[l_pointer] in vowels and s[r_pointer] in vowels:
                output[l_pointer], output[r_pointer] = (
                    output[r_pointer],
                    output[l_pointer],
                )
                l_pointer += 1
                r_pointer -= 1
            elif s[l_pointer] in vowels:
                r_pointer -= 1
            elif s[r_pointer] in vowels:
                l_pointer += 1
            else:
                l_pointer += 1
                r_pointer -= 1
        return "".join(output)
