""" https://leetcode.com/problems/binary-tree-cameras/
post-order traversal, there are three conditions for any node:
0 - leaf node
1 - covered node without camera
2 - covered node with camera 
"""
class Solution:
    def minCameraCover(self, root: Optional[TreeNode]) -> int:
        self.ans = 0
        
        def dfs(node):
            if not node: return 1
            l, r = dfs(node.left), dfs(node.right)
            # if any children not covered, then monitor it
            if l==0 or r==0:
                self.ans += 1
                return 2
            # if any children is covered, then no need to monitor it
            if l==2 or r==2: return 1
            return 0