""" https://leetcode.com/problems/implement-trie-ii-prefix-tree/
slightly modify trie
"""


class Trie:
    def __init__(self):
        self.trie = {}

    def insert(self, word: str) -> None:
        t = self.trie
        for c in word:
            if c not in t:
                t[c] = {"cnt": 0}
            t[c]["cnt"] += 1
            t = t[c]
        t["#"] = t.get("#", 0) + 1

    def countWordsEqualTo(self, word: str) -> int:
        t = self.trie
        for c in word:
            if c not in t:
                return 0
            t = t[c]
        return t.get("#", 0)

    def countWordsStartingWith(self, prefix: str) -> int:
        t = self.trie
        for p in prefix:
            if p not in t:
                return 0
            t = t[p]
        return t["cnt"]

    def erase(self, word: str) -> None:
        t = self.trie
        for w in word:
            if w not in t:
                return
            t[w]["cnt"] = max(0, t[w]["cnt"] - 1)
            t = t[w]
        t["#"] = max(0, t["#"] - 1)
