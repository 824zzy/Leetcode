""" https://leetcode.com/problems/symmetric-tree/
use level order traversal check if every layer is palindrome
"""
class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        Q = [root]
        while Q:
            nextQ = []
            v = []
            for n in Q:
                if n.left: v.append(n.left.val)
                else: v.append(None)
                if n.right: v.append(n.right.val)
                else: v.append(None)
                if n.left: nextQ.append(n.left)
                if n.right: nextQ.append(n.right)
            if v!=v[::-1]: return False
            Q = nextQ
        return True