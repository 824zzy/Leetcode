""" https://leetcode.com/problems/binary-tree-paths/submissions/
"""


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []

        def dfs(node, path):
            if not node:
                return
            if not node.left and not node.right:
                return ans.append(path + str(node.val))
            dfs(node.left, path + str(node.val) + '->')
            dfs(node.right, path + str(node.val) + '->')

        dfs(root, '')
        return ans
