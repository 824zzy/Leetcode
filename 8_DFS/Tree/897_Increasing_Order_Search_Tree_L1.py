""" https://leetcode.com/problems/increasing-order-search-tree/
learn from lee: https://leetcode.com/problems/increasing-order-search-tree/discuss/165885/C%2B%2BJavaPython-Self-Explained-5-line-O(N)
ans = inorder(node.left) + node + inorder(node.right)
"""
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        def dfs(node, prev=None):
            if not node: return prev
            ans = dfs(node.left, node)
            node.left = None
            node.right = dfs(node.right, prev)
            return ans
        
        return dfs(root)
    

# straight forward solution
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        self.ans = self.curr = TreeNode(0)
        def dfs(node):
            if not node: return
            dfs(node.left)
            self.curr.right = TreeNode(node.val)
            self.curr = self.curr.right
            dfs(node.right)
        
        dfs(root)
        return self.ans.right