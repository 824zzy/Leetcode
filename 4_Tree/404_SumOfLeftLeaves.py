# Facebook
class Solution:
    ans = 0
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return
            if not node.left and not node.right:
                return node.val
            left = dfs(node.left)
            right = dfs(node.right)
            if left:
                self.ans += left
        dfs(root)
        return self.ans
    
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(node):
            if not node:
                return
            if node.left and not node.left.right and not node.left.left:
                self.ans += node.left.val
            dfs(node.left)
            dfs(node.right)
                
        dfs(root)
        return self.ans