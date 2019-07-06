""" Take care of max(l, r, 0), the case of all negative child should return 0
"""
# time consuming saving space
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            if not node:
                return float('-inf')
            
            l, r = dfs(node.left), dfs(node.right)
            self.ans = max(self.ans, node.val, node.val+l+r, node.val+l, node.val+r)
            
            return max(l, r, 0)+node.val    
        
        self.ans = float('-inf')
        dfs(root)
        return self.ans

# space consuming saving time
class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        def dfs(node: TreeNode):
            if not node:
                return 0
            
            l, r = dfs(node.left), dfs(node.right)
            self.ans.append(max(node.val, node.val+l+r, node.val+l, node.val+r))
            
            return max(l, r, 0)+node.val    
        
        self.ans = []
        dfs(root)
        return max(self.ans)