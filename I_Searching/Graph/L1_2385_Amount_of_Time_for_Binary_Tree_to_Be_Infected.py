""" https://leetcode.com/problems/amount-of-time-for-binary-tree-to-be-infected/
two pass

It is easier to treat the problem as a graph problem:
1. build graph by dfs
2. find maximum second by bfs
"""
from header import *

class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # build graph by dfs
        G = defaultdict(list)
        def dfs(node, prev):
            if not node: return 
            if prev:
                G[prev.val].append(node.val)
                G[node.val].append(prev.val)
            dfs(node.left, node)
            dfs(node.right, node)
            
        dfs(root, None)

        # find maximum second by bfs
        Q = [start]
        seen = {start}
        ans = 0
        while Q:
            for _ in range(len(Q)):
                i = Q.pop(0)
                for j in G[i]:
                    if j not in seen:
                        seen.add(j)
                        Q.append(j)
            ans += 1
        return ans-1