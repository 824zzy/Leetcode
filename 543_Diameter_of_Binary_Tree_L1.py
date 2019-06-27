""" Seperate Function
"""
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans = 0
        self.depth(root)
        return self.ans

    def depth(self, node: TreeNode) -> int:
        if not node:
            return 0
        left = self.depth(node.left)
        right = self.depth(node.right)
        self.ans = max(self.ans, left+right)
        return 1+max(left, right)

""" Nested Function
"""
class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.res = 0
        def depth(node: TreeNode) -> int:
            if not node:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.res = max(self.res, left+right)
            return 1+max(left, right)
        depth(root)
        return self.res