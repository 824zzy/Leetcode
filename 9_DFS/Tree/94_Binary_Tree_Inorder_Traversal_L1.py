# Iterative solution
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        curr = root
        stk, ans = [], []
        while stk or curr:
            while curr:
                stk.append(curr)
                curr = curr.left
            curr = stk.pop()
            ans.append(curr.val)
            curr = curr.right            
        return ans

# Recursive solution
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        self.ans = []
        
        def dfs(node):
            if not node: return
            dfs(node.left)
            self.ans.append(node.val)
            dfs(node.right)
        
        dfs(root)