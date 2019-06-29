""" Recursive trick of check left child
if root.left and not root.left.left and not root.left.right
"""
# neat one
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        if not root:
            return 0
        elif root.left and not root.left.left and not root.left.right:
            return root.left.val + self.sumOfLeftLeaves(root.right)
        else:
            return self.sumOfLeftLeaves(root.left) + self.sumOfLeftLeaves(root.right)

# another solution by zzy824
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.ans = 0

        def dfs(node: TreeNode) -> None:
            if not node:
                return
            if node.left and not node.left.left and not node.left.right:
                self.ans += node.left.val
            
            dfs(node.left)
            dfs(node.right)
        
        dfs(root)
        return self.ans