""" https://leetcode.com/problems/minimum-depth-of-binary-tree/
"""
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        def dfs(node, depth):
            if not node:
                return float('inf')
            if not node.left and not node.right:
                return depth
            left = dfs(node.left, depth+1)
            right = dfs(node.right, depth+1)
            return min(left, right)
        return dfs(root, 1)
    
        
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.ans = float('inf')
        def dfs(node, d):
            if not node:
                return
            if not node.left and not node.right:
                self.ans = min(d+1, self.ans)
                return
            dfs(node.left, d+1)
            dfs(node.right, d+1)
        dfs(root, 0)
        return self.ans
    
    
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        d = 1
        q = [(root, d)]
        while q:
            cur, dep = q.pop(0)
            if not cur.left and not cur.right:
                return dep
            if cur.left:
                q.append((cur.left, dep+1))
            if cur.right:
                q.append((cur.right, dep+1))