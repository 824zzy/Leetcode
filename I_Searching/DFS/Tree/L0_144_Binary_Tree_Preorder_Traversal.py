""" https://leetcode.com/problems/binary-tree-preorder-traversal/
tree dfs algorithm template
"""


class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        self.ans = []

        def dfs(node):
            if not node:
                return
            self.ans.append(node.val)
            dfs(node.left)
            dfs(node.right)
        dfs(root)
        return self.ans
