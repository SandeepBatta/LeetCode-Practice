# # Problem Statement
# You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots.
# Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise.


class Solution:
    def canPlaceFlowers(self, flowerbed: list[int], n: int) -> bool:
        if n == 0:
            return True
        for idx in range(len(flowerbed)):
            if (
                flowerbed[idx] == 0
                and (True if idx == 0 else flowerbed[idx - 1] == 0)
                and (True if idx == len(flowerbed) - 1 else flowerbed[idx + 1] == 0)
            ):
                flowerbed[idx] = 1
                n = n - 1
                if n == 0:
                    return True
        return False
