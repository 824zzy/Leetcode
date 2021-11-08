""" L0: https://leetcode.com/problems/same-tree/
traverse two trees to find different node
"""
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def dfs(p, q):
            if not p and not q: return True
            if not p or not q or (p.val!=q.val): return False
            l = dfs(p.left, q.left)
            r = dfs(p.right, q.right)
            return l and r
        
        return dfs(p, q)