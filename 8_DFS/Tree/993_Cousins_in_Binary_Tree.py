""" L0: https://leetcode.com/problems/cousins-in-binary-tree/
record x and y's parent and depth
"""
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        self.A, self.B = [0, 0], [0, 0]
        def dfs(node, prev, d):
            if not node: return
            
            if node.val==x: self.A = [prev, d]
            elif node.val==y: self.B = [prev, d]
            
            dfs(node.left, node, d+1)
            dfs(node.right, node, d+1)
        
        dfs(root, None, 0)
        return self.A[1]==self.B[1] and self.A[0]!=self.B[0]