""" https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/
"""
from header import *

class Solution:
    def isValidSequence(self, root: Optional[TreeNode], A: List[int]) -> bool:
        def dfs(node, i):
            if not node or i==len(A) or node.val!=A[i]: return False
            if not node.left and not node.right:
                return i==len(A)-1
            
            return dfs(node.left, i+1) or dfs(node.right, i+1)
        
        return dfs(root, 0)
    
"""
[0,1,0,0,1,0,null,null,1,0,0]
[0,1,0,1]
[0,1,0,0,1,0,null,null,1,0,0]
[0,0,1]
[0,1,0,0,1,0,null,null,1,0,0]
[0,1,1]
[5,6,9,null,null,5,4,null,5,null,3]
[5]
"""