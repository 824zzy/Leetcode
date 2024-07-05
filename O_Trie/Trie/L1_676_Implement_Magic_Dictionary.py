""" https://leetcode.com/problems/implement-magic-dictionary/
The trie solution can be used to solve this problem even the data size is large.

Time complexity: O(100*n)
"""


class MagicDictionary:
    def __init__(self):
        self.trie = {}

    def buildDict(self, dictionary: List[str]) -> None:
        for w in dictionary:
            node = self.trie
            for c in w:
                if c not in node:
                    node[c] = {}
                node = node[c]
            node["#"] = w

    def search(self, w: str) -> bool:
        def dfs(node, i, change):
            if not node:
                return False
            if i == len(w):
                return "#" in node and change
            if change:
                return dfs(node.get(w[i]), i + 1, True)
            else:
                ans = False
                for c in node:
                    if c != "#":
                        ans |= dfs(node[c], i + 1, c != w[i])
                return ans

        return dfs(self.trie, 0, False)
