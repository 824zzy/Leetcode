""" https://leetcode.com/problems/count-good-nodes-in-binary-tree/
count nodes whose value larger than threshold.
"""
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.ans = 0
        
        def dfs(node, mx):
            if not node: return
            if node.val>=mx: self.ans += 1
            dfs(node.left, max(mx, node.val))
            dfs(node.right, max(mx, node.val))
            
        dfs(root, -inf)
        return self.ans