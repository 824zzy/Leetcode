""" L0: https://leetcode.com/problems/sum-root-to-leaf-numbers/
find leaves and calculate sum 
"""
class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node, p):
            if not node: return
            if not node.left and not node.right:
                self.ans += int(p+str(node.val))
                return
            dfs(node.left, p+str(node.val))
            dfs(node.right, p+str(node.val))
        
        dfs(root, "")
        return self.ans