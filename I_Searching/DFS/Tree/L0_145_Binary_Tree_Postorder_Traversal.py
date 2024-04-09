""" https://leetcode.com/problems/binary-tree-postorder-traversal/
tree dfs algorithm template
"""


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
