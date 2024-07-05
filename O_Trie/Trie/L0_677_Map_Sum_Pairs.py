""" L0: https://leetcode.com/problems/map-sum-pairs/
1. build a trie to save keys
2. use bfs/dfs to find sum of subtrie
"""


class MapSum:
    def __init__(self):
        self.trie = {}

    def insert(self, k: str, v: int) -> None:
        node = self.trie
        for c in k:
            if c not in node:
                node[c] = {}
            node = node[c]
        node["#"] = v

    def sum(self, prefix: str) -> int:
        # find the node start with prefix
        node = self.trie
        ans = 0
        for c in prefix:
            if c not in node:
                return ans
            node = node[c]
        # compute the sum of the node's subtrie
        Q = [node]
        while Q:
            i = Q.pop()
            for k, v in i.items():
                if k == "#":
                    ans += v
                else:
                    Q.append(v)
        return ans
