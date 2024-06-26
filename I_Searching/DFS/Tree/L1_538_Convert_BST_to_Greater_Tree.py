""" https://leetcode.com/problems/convert-bst-to-greater-tree/
use a global sum to update node value in inorder traversal
"""


class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        self.sum = 0

        def dfs(node):
            if not node:
                return 0
            dfs(node.right)
            self.sum += node.val
            node.val = self.sum
            dfs(node.left)

        dfs(root)
        return root
