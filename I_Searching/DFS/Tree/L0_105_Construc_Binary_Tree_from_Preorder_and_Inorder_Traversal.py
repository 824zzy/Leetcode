""" https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""


class Solution:
    def buildTree(self, P: List[int], I: List[int]) -> Optional[TreeNode]:
        def dfs(P, I):
            if len(I) == 0:
                return None
            val = P.pop(0)
            idx = I.index(val)
            node = TreeNode(val)
            node.left = dfs(P, I[:idx])
            node.right = dfs(P, I[idx + 1 :])
            return node

        return dfs(P, I)
