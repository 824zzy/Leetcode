""" https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/
build tree by finding middle index numbers
"""


class Solution:
    def sortedArrayToBST(self, A: List[int]) -> Optional[TreeNode]:
        def dfs(A):
            if not A:
                return None
            node = TreeNode(A[len(A) // 2])
            node.left = dfs(A[:len(A) // 2])
            node.right = dfs(A[len(A) // 2 + 1:])
            return node

        return dfs(A)
