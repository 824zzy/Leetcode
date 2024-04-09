""" https://leetcode.com/problems/design-hashmap/
Multiplicative hashing:  https://en.wikipedia.org/wiki/Hash_function#Multiplicative_hashing

h(K) = (aK mod 2**w) / 2**(w-m), where K is key, a is big prime number, m is length of output(10000), w is size of machine word.
In practice, this function becomes h(K) = (aK) >> (w-m).
"""
# chaining


class MyHashMap:
    def __init__(self):
        self.m = [[] for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        for i, (k, v) in enumerate(self.m[key % 1000]):
            if k == key:
                self.m[key % 1000][i] = (k, value)
                break
        else:
            self.m[key % 1000].append((key, value))

    def get(self, key: int) -> int:
        for k, v in self.m[key % 1000]:
            if k == key:
                return v
        return -1

    def remove(self, key: int) -> None:
        for k, v in self.m[key % 1000]:
            if k == key:
                self.m[key % 1000].remove((key, v))
