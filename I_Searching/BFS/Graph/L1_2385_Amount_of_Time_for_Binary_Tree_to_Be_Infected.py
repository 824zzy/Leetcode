""" https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/
two pass + bfs + dfs

It is easier to treat the problem as a graph problem:
1. build graph by dfs
2. find maximum second by bfs
"""
from header import *


class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        G = defaultdict(list)

        def dfs(node):
            if node.left:
                G[node.val].append(node.left.val)
                G[node.left.val].append(node.val)
                dfs(node.left)
            if node.right:
                G[node.val].append(node.right.val)
                G[node.right.val].append(node.val)
                dfs(node.right)

        dfs(root)

        Q = [start]
        seen = {start}
        ans = 0
        while Q:
            nxtQ = []
            for x in Q:
                for j in G[x]:
                    if j not in seen:
                        seen.add(j)
                        nxtQ.append(j)
            Q = nxtQ
            ans += 1
        return ans - 1
