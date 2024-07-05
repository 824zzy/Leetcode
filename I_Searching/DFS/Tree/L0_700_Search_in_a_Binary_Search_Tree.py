""" https://leetcode.com/problems/search-in-a-binary-search-tree/submissions/
"""


class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        def dfs(node):
            if not node:
                return None

            if node.val == val:
                return node
            elif node.val > val:
                ans = dfs(node.left)
            else:
                ans = dfs(node.right)

            return ans

        return dfs(root)
