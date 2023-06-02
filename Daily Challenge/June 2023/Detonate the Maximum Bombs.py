# # Challenge Context
# You are given a list of bombs. The range of a bomb is defined as the area where its effect can be felt. This area is in the shape of a circle with the center as the location of the bomb.
# The bombs are represented by a 0-indexed 2D integer array bombs where bombs[i] = [xi, yi, ri]. xi and yi denote the X-coordinate and Y-coordinate of the location of the ith bomb, whereas ri denotes the radius of its range.
# You may choose to detonate a single bomb. When a bomb is detonated, it will detonate all bombs that lie in its range. These bombs will further detonate the bombs that lie in their ranges.
# Given the list of bombs, return the maximum number of bombs that can be detonated if you are allowed to detonate only one bomb.

# Challenge Link --> https://leetcode.com/problems/detonate-the-maximum-bombs/

import math


class Solution:
    def maximumDetonation(self, bombs: list[list[int]]) -> int:
        n = len(bombs)
        bombs_detonated = [1 for _ in range(n)]
        graph = [[] for _ in range(n)]

        # Build the graph
        for i in range(n):
            for j in range(n):
                xi, yi, ri = bombs[i]
                xj, yj, _ = bombs[j]

                # Create a path from i to j, if bomb i detonates bomb j.
                if ri**2 >= (xi - xj) ** 2 + (yi - yj) ** 2:
                    graph[i].append(j)

        for idx in range(n):
            visited = set([idx])
            stack = [idx]
            while stack:
                b = stack.pop()
                for idx2 in graph[b]:
                    if idx2 not in visited:
                        visited.add(idx2)
                        stack.append(idx2)
                        bombs_detonated[idx] = bombs_detonated[idx] + 1

        return max(bombs_detonated)
