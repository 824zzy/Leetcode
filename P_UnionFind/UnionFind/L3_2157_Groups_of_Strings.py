""" https://leetcode.com/problems/groups-of-strings/
union find + bit mask
Extremely hard.
"""


class DSU:
    def __init__(self, n):
        self.p = list(range(n))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        self.p[self.find(x)] = self.find(y)


class Solution:
    def groupStrings(self, words: List[str]) -> List[int]:
        n, dsu = len(words), DSU(len(words))
        dt = dict()

        for i, w in enumerate(words):
            x = sum(1 << (ord(c) - ord("a")) for c in w)
            # identical words
            if x in dt:
                dsu.union(i, dt[x])

            # if two words are connected by replacement, they have same child
            # after deleting 1 letter
            for j in range(26):
                if x & (1 << j):
                    y = x ^ (1 << j)
                    if y in dt:
                        dsu.union(i, dt[y])
                    dt[y] = i
            dt[x] = i

        count = Counter(dsu.find(i) for i in range(n))
        return [len(count), max(count.values())]
