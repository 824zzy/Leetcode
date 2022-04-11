""" https://leetcode.com/problems/recover-binary-search-tree/
solution from ye: https://leetcode.com/problems/recover-binary-search-tree/discuss/689225/Python3-is-O(1)-space-possible
Iteratively in-order traverse the tree. 
For a valid BST, the output should be in ascending order. 
Locate the two nodes where the symmetric order is violated, and swap their values.
"""
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        node, stk = root, []
        pre = l = r = None
        while stk or node:
            if node:
                stk.append(node)
                node = node.left
                continue
            node = stk.pop()
            if pre and pre.val>node.val:
                if not l: l, r = pre, node
                else: r = node
            pre = node
            node = node.right
        l.val, r.val = r.val, l.val