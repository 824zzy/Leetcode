""" https://leetcode.com/problems/number-of-nodes-in-the-sub-tree-with-the-same-label/
post order dfs. At each node, update seen table by subtree's seen table.
"""
from header import *


class Solution:
    def countSubTrees(self,
                      n: int,
                      edges: List[List[int]],
                      labels: str) -> List[int]:
        G = defaultdict(list)
        for i, j in edges:
            G[i].append(j)
            G[j].append(i)
        ans = [0] * len(labels)

        def dfs(i, p):
            seen = [0] * 26
            seen[ord(labels[i]) - 97] = 1
            for j in G[i]:
                if j != p:
                    _seen = dfs(j, i)
                    for x in range(len(seen)):
                        seen[x] += _seen[x]
            ans[i] = seen[ord(labels[i]) - 97]
            return seen

        dfs(0, None)
        return ans
