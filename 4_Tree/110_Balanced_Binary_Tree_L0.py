class Solution:
    def isBalanced(self, root: TreeNode, d=0) -> bool:
        self.ans = True
        def dfs(node, d):
            if not node: return d
            l = dfs(node.left, d+1)
            r = dfs(node.right, d+1)
            if abs(l-r)>1: self.ans = False
            return max(l, r)
        dfs(root, 0)
        return self.ans
    
    
    
class Solution:
    def isBalanced(self, root: TreeNode, d=0) -> bool:
        self.ans = True
        def dfs(node, d):
            if not node: return d
            l = dfs(node.left, d+1)
            r = dfs(node.right, d+1)
            # add code here
            return max(l, r)
        dfs(root, 0)
        return self.ans