""" L1: https://leetcode.com/problems/smallest-subtree-with-all-the-deepest-nodes/submissions/
get subtree deepest depth, same idea of 1123
"""
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        self.ans = 0
        self.D = 0
        
        def dfs(node, d):
            self.D = max(d, self.D)
            if not node: return d
            
            l, r = dfs(node.left, d+1), dfs(node.right, d+1)
            if l==r==self.D: self.ans = node
            return max(l, r)
        
        dfs(root, 0)
        return self.ans