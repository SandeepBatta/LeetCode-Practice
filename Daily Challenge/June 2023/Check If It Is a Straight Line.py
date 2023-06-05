# # Challenge Context
# You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.

# Challenge Link --> https://leetcode.com/problems/check-if-it-is-a-straight-line/


class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        slope = float("inf") if x1 - x0 == 0 else (y1 - y0) / (x1 - x0)

        for i in range(1, len(coordinates) - 1):
            xi, yi = coordinates[i]
            xj, yj = coordinates[i + 1]

            if slope != (float("inf") if xj - xi == 0 else (yj - yi) / (xj - xi)):
                return False

        return True
