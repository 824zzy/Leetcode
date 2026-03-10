""" L1: https://leetcode.com/problems/lexicographical-numbers/
trie+dfs
Note that don't write "n not in self.ans", it is not necessart.
"""


class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        self.trie = {}

        def insert(word):
            cur = self.trie
            for w in word:
                if w not in cur:
                    cur[w] = {}
                cur = cur[w]
            cur["#"] = "x"

        for i in range(1, n + 1):
            insert(str(i))

        self.ans = []

        def dfs(n, T):
            if "#" in T:
                self.ans.append(int(n))

            for k, v in T.items():
                if k != "#":
                    dfs(n + k, T[k])

        dfs("", self.trie)
        return self.ans
