""" https://leetcode.com/problems/evaluate-boolean-binary-tree/
dfs template on tree with boolean
"""


class Solution:
    def evaluateTree(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node.left and not node.right:
                return node.val
            l = dfs(node.left)
            r = dfs(node.right)

            if node.val == 2:
                return l or r
            elif node.val == 3:
                return l and r

        return dfs(root)
