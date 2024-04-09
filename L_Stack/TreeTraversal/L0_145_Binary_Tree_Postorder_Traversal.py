""" https://leetcode.com/problems/binary-tree-postorder-traversal/
"""
# iterative solution


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        stk1 = [root]
        stk2 = []
        ans = []
        while stk1:
            node = stk1.pop()
            if node.left:
                stk1.append(node.left)
            if node.right:
                stk1.append(node.right)
            stk2.append(node)
        while stk2:
            ans.append(stk2.pop().val)
        return ans

# recursive solution


class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            dfs(node.right)
            ans.append(node.val)

        dfs(root)
        return ans
