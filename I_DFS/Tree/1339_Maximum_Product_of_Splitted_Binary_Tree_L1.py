""" https://leetcode.com/problems/maximum-product-of-splitted-binary-tree/
Observation: f(x) = (all_sum-subtree_sum)*subtree_sum
1. one dfs for calculating the sum of all nodes
2. another dfs for calculating the subtree sum and the product of (all_sum-subtree_sum)*subtree_sum
"""
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def dfs(node):
            if not node: return 0
            sm = node.val
            sm += dfs(node.left)
            sm += dfs(node.right)
            return sm
        
        self.all_sum = dfs(root)
        
        def dfs(node):
            if not node: return 0
            l = dfs(node.left)
            r = dfs(node.right)
            subtree_sum = l+r+node.val
            self.ans = max(self.ans, (self.all_sum-subtree_sum)*subtree_sum)
            return subtree_sum
        
        self.ans = 0
        dfs(root)
        return self.ans%(10**9+7)