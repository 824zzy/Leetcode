""" L3: https://leetcode.com/problems/binary-tree-cameras/
tri-color encoding
0 - not covered 
1 - covered w/o camera
2 - covered w/ camera 
"""
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        def dfs(node):
            if not node: return 1
            l = dfs(node.left)
            r = dfs(node.right)
            if l==0 or r==0: 
                self.ans += 1
                return 2
            if l==2 or r==2: return 1
            return 0