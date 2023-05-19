""" https://leetcode.com/problems/binary-tree-pruning/
"""
class Solution:
    def pruneTree(self, root):
        def dfs(node):
            if not node: return False   
            l = dfs(node.left)
            r = dfs(node.right)
            if not l: 
                node.left = None
            if not r:
                node.right = None
            return node.val or l or r
            
        return root if dfs(root) else None
            
"""
[1,null,0,0,1]
[1,0,1,0,0,0,1]
[1,1,0,1,1,0,1,0]
[0,null,0,0,0]
"""