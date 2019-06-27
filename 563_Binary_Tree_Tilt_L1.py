""" Naive Recursive Solution
"""
class Solution:
    def findTilt(self, root: TreeNode) -> int:
        self.ans = 0
        
        def dfs(node: TreeNode) -> Node:
            if not node:
                return 0
            left = dfs(node.left) 
            right = dfs(node.right)
            self.ans += abs(left-right)
            return node.val+left+right
        
        dfs(root)
        
        return self.ans