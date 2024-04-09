""" https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
the same as 102, but use a reverse flag to control zigzag shape
"""
from header import *


class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:
            return []
        queue = [root]
        reverse = 0
        ans = []
        while queue:
            cur = []
            for _ in range(len(queue)):
                n = queue.pop(0)
                cur.append(n.val)
                if n.left:
                    queue.append(n.left)
                if n.right:
                    queue.append(n.right)
            reverse += 1
            if reverse % 2 != 0:
                ans.append(cur)
            else:
                ans.append(cur[::-1])
        return ans
