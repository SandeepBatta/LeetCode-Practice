# # Challenge Context
# Design a HashSet without using any built-in hash table libraries.

# Challenge Link --> https://leetcode.com/problems/design-hashset/


# Used chaining to handle collisions
class MyHashSet:
    def __init__(self):
        self.size = 1000
        self.hashes = [[] for _ in range(self.size)]

    # Set the hash index for key between 0 to 1000
    def _hash_function(self, key: int) -> int:
        return key % self.size

    def add(self, key: int) -> None:
        if not self.contains(key):
            idx = self._hash_function(key)
            self.hashes[idx].append(key)

    def remove(self, key: int) -> None:
        idx = self._hash_function(key)
        for k_idx, k in enumerate(self.hashes[idx]):
            if k == key:
                self.hashes[idx].pop(k_idx)
                break

    def contains(self, key: int) -> bool:
        idx = self._hash_function(key)
        for k in self.hashes[idx]:
            if k == key:
                return True
        return False


# Your MyHashSet object will be instantiated and called as such:
# obj = MyHashSet()
# obj.add(key)
# obj.remove(key)
# param_3 = obj.contains(key)
