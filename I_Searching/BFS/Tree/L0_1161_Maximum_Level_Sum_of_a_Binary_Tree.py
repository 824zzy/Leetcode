""" https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
traverse level by level, keep track of the max sum and the level
"""
from header import *

class Solution:
    def maxLevelSum(self, root: Optional[TreeNode]) -> int:
        Q = [root]
        mx = -inf
        d = 0
        ans = 0
        while Q:
            nxt = []
            sm = 0
            d += 1
            for node in Q:
                sm += node.val
                if node.left:
                    nxt.append(node.left)
                if node.right:
                    nxt.append(node.right)
            Q = nxt
            if sm>mx:
                mx = max(mx, sm)
                ans = d
        return ans