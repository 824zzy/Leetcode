""" https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
learn from dba: https://leetcode.com/problems/flatten-binary-tree-to-linked-list/discuss/1207839/Python-Intuitive-solution-explained
record begin and end of link list segment during dfs
"""


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def dfs(node):
            if not node:
                return (None, None)
            lb, le = dfs(node.left)
            rb, re = dfs(node.right)
            node.left = None

            if not le and not re:
                return (node, node)
            if not le and re:
                node.right = rb
                return (node, re)
            if le and not re:
                node.right = lb
                return (node, le)
            else:
                node.right = lb
                le.right = rb
                return (node, re)

        dfs(root)


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        def dfs(node, tail=None):
            if not node:
                return tail
            node.right = dfs(node.left, dfs(node.right, tail))
            node.left = None
            return node

        dfs(root)
