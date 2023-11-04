""" https://leetcode.com/problems/find-largest-value-in-each-tree-row/
simulation using dfs/bfs
"""
from header import *

# dfs
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        T = defaultdict(list)
        
        def dfs(node, d):
            if not node:
                return
            T[d].append(node.val)
            dfs(node.left, d+1)
            dfs(node.right, d+1)
        dfs(root, 0)
        return [sorted(v)[-1] for k, v in T.items()]
    

# bfs
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root: return []
        Q = [root]
        ans = []
        while Q:
            nxtQ = []
            mx = -inf
            for node in Q:
                mx = max(mx, node.val)
                if node.left:
                    nxtQ.append(node.left)
                if node.right:
                    nxtQ.append(node.right)
            ans.append(mx)
            Q = nxtQ
        return ans