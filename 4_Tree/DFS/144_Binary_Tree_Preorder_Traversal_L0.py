class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.ans = []
        def dfs(node):
            if not node: return 
            self.ans.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.ans
    
    
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        ans, stk = [], []
        node = root
        while stk or node:
            while node:
                stk.append(node)
                ans.append(node.val)
                node = node.left
            node = stk.pop()
            node = node.right
        return ans