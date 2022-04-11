""" https://leetcode.com/problems/binary-tree-preorder-traversal/
"""
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stk = []
        node = root
        
        while stk or node:
            if node: 
                ans.append(node.val)
                stk.append(node)
                node = node.left
            else:
                node = stk.pop()
                node = node.right
        return ans
    
    
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
