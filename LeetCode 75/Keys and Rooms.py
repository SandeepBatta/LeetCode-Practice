# # Problem Statement
# There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to visit all the rooms. However, you cannot enter a locked room without having its key.
# When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which room it unlocks, and you can take all of them with you to unlock the other rooms.
# Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true if you can visit all the rooms, or false otherwise.


class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        rooms_visited = [False for _ in rooms]

        # Assume it like a queue
        room_keys_explore = []

        # Lets start BFS algorithm with room 0
        room = 0
        rooms_visited[room] = True
        room_keys_explore.append(room)

        # Repeat till our queue is empty
        while room_keys_explore:
            room = room_keys_explore.pop(0)
            for room in rooms[room]:
                if rooms_visited[room] == False:
                    room_keys_explore.append(room)
                    rooms_visited[room] = True

        return all(rooms_visited)
