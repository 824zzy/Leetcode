""" https://leetcode.com/problems/most-profitable-path-in-a-tree/description/
two dfs:
1. dfs1: calculate the distance from bob to 0
2. dfs2: calculate the maximum profit Alice can get from 0 to leaf
"""
from header import *

# general form


class Solution:
    def mostProfitablePath(self,
                           edges: List[List[int]],
                           bob: int,
                           amount: List[int]) -> int:
        G = defaultdict(list)
        for i, j in edges:
            G[i].append(j)
            G[j].append(i)

        timestamp = [inf] * len(amount)
        seen = [False] * len(amount)
        seen[0] = True
        self.path = []

        def dfs(i):
            if i == bob:
                timestamp[bob] = 0
                return 0

            ans = inf
            for j in G[i]:
                if not seen[j]:
                    seen[j] = True
                    tmp = dfs(j)
                    ans = min(ans, tmp + 1)
            timestamp[i] = ans
            return ans
        dfs(0)

        seen = [False] * len(amount)
        seen[0] = True
        self.ans = -inf

        def dfs(i, ts, p):
            if ts < timestamp[i]:
                p += amount[i]
            elif ts == timestamp[i]:
                p += amount[i] // 2
            # leaf node
            if len(G[i]) == 1 and i != 0:
                self.ans = max(self.ans, p)

            for j in G[i]:
                if not seen[j]:
                    seen[j] = True
                    dfs(j, ts + 1, p)
        dfs(0, 0, 0)
        return self.ans


# post order traversal from ye
class Solution:
    def mostProfitablePath(self,
                           edges: List[List[int]],
                           bob: int,
                           amount: List[int]) -> int:
        n = 1 + len(edges)
        tree = [[] for _ in range(n)]
        for u, v in edges:
            tree[u].append(v)
            tree[v].append(u)
        seen = [False] * n

        def dfs(u, d):
            """Return """
            seen[u] = True
            ans = -inf
            dd = 0 if u == bob else n
            for v in tree[u]:
                if not seen[v]:
                    x, y = dfs(v, d + 1)
                    ans = max(ans, x)
                    dd = min(dd, y)
            if ans == -inf:
                ans = 0
            if d == dd:
                ans += amount[u] // 2
            if d < dd:
                ans += amount[u]
            return ans, dd + 1

        return dfs(0, 0)[0]
