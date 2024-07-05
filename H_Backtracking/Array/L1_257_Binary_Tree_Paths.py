""" https://leetcode.com/problems/binary-tree-paths/
"""


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        ans = []
        stk = []

        def dfs(node):
            if not node:
                return
            stk.append(str(node.val))
            if not node.left and not node.right:
                ans.append("->".join(stk.copy()))
            dfs(node.left)
            dfs(node.right)
            stk.pop()

        dfs(root)
        return ans
