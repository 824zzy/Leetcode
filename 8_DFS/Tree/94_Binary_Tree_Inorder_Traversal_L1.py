""" https://leetcode.com/problems/binary-tree-inorder-traversal/
"""
# Iterative solution
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        stk = []
        ans = []
        node = root
        while stk or node:
            if node:
                stk.append(node)
                node = node.left
            else:
                node = stk.pop()
                ans.append(node.val)
                node = node.right
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