""" L0: template
count nodes whose value larger than threshold.
"""
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        def dfs(node, t):
            if not node: return
            if node.val>=t: 
                self.ans += 1
                t = node.val
            dfs(node.left, t)
            dfs(node.right, t)
        
        dfs(root, root.val)
        return self.ans
