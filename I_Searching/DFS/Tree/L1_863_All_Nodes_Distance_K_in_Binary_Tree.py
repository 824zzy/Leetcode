""" https://leetcode.com/problems/all-nodes-distance-k-in-binary-tree/
Two pass iteration:
1. One pass to build the graph
2. One pass to BFS the graph to find the nodes with distance k from target node
"""
from header import *


class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        G = defaultdict(list)

        def dfs(node, p):
            if not node:
                return
            if p:
                G[p].append(node)
                G[node].append(p)
            dfs(node.left, node)
            dfs(node.right, node)
        dfs(root, None)

        Q = [(target, k)]
        ans = []
        seen = {target.val}
        while Q:
            i, rem = Q.pop(0)
            if rem == 0:
                ans.append(i.val)
            for j in G[i]:
                if j.val not in seen:
                    seen.add(j.val)
                    Q.append([j, rem - 1])
        return ans
