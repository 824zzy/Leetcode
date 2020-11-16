# Amazon
class Solution:
    def rangeSumBST(self, root: TreeNode, L: int, R: int) -> int:
        self.ans = 0
        def dfs(node):
            if not node:
                return
            if L<=node.val<=R:
                self.ans += node.val
            dfs(node.left)
            dfs(node.right)
            
        dfs(root)
        return self.ans

class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        self.ans = 0
        def dfs(node):
            if not node:
                return
            if low<=node.val<=high:
                self.ans += node.val
                dfs(node.left)
                dfs(node.right)
            elif node.val<low:
                dfs(node.right)
            elif node.val>high:
                dfs(node.left)
                
        dfs(root)
        return self.ans