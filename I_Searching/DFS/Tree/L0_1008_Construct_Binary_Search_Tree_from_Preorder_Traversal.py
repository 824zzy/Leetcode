""" L0: https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
dfs+bisect to seperate left and right children.
"""


class Solution:
    def bstFromPreorder(self, preorder: List[int]) -> Optional[TreeNode]:
        def dfs(vals):
            if not vals:
                return None
            v = vals.pop(0)
            node = TreeNode(v)
            idx = bisect_left(vals, v)
            node.left = dfs(vals[:idx])
            node.right = dfs(vals[idx:])
            return node

        return dfs(preorder)
