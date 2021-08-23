""" L0: template
Use set T to find target value.
"""
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        T = set()
        
        def dfs(node):
            if not node: return False
            if node.val in T: return True
            l, r = False, False
            T.add(k-node.val)
            l = dfs(node.left)
            r = dfs(node.right)
            return l or r
        
        return dfs(root)