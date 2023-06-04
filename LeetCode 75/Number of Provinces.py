# # Problem Statement
# There are n cities. Some of them are connected, while some are not. If city a is connected directly with city b, and city b is connected directly with city c, then city a is connected indirectly with city c.
# A province is a group of directly or indirectly connected cities and no other cities outside of the group.
# You are given an n x n matrix isConnected where isConnected[i][j] = 1 if the ith city and the jth city are directly connected, and isConnected[i][j] = 0 otherwise.
# Return the total number of provinces.


class Solution:
    def __init__(self):
        self.cities_visited = set()

    def bfs(self, city, cities_graph):
        self.cities_visited.add(city)
        queue = [city]
        while queue:
            c = queue.pop(0)
            for i in cities_graph[c]:
                if i not in self.cities_visited:
                    self.cities_visited.add(i)
                    queue.append(i)

    def findCircleNum(self, isConnected: list[list[int]]) -> int:
        rows, cols = len(isConnected), len(isConnected[0])

        cities_graph = [[] for _ in range(rows)]

        for i in range(rows):
            for j in range(cols):
                if i != j and isConnected[i][j] == 1:
                    cities_graph[i].append(j)

        provinces = 0

        for city in range(rows):
            if city not in self.cities_visited:
                self.bfs(city, cities_graph)
                provinces += 1

        return provinces
