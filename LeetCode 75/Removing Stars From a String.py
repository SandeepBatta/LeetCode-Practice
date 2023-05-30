# # Problem Statement
# You are given a string s, which contains stars *.

# In one operation, you can:
# 1) Choose a star in s.
# 2) Remove the closest non-star character to its left, as well as remove the star itself.

# Return the string after all stars have been removed.


# Solution 1
# class Solution:
#     def removeStars(self, s: str) -> str:
#         output = s
#         while True:
#             star_idx = output.find("*")
#             if star_idx == -1:
#                 return output
#             else:
#                 output = output[: star_idx - 1] + output[star_idx + 1 :]


# Solution 2
class Solution:
    def removeStars(self, s: str) -> str:
        output = []
        # append the non '*' char into stack and pop the last element if the char is '*'
        for char in s:
            if char == "*":
                # will get an error if '*' is the first element of string. In the problem statement, they clearly mentioned that non-star char is always present before '*'
                output.pop()
            else:
                output.append(char)
        return "".join(output)
