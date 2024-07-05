""" https://leetcode.com/problems/recover-a-tree-from-preorder-traversal/
preprocess the string and use dfs to construct the tree
"""


class Solution:
    def recoverFromPreorder(self, s: str) -> Optional[TreeNode]:
        A = []
        s = s.split("-")
        for i in range(len(s)):
            if s[i].isnumeric():
                A.append(")")
                A.append(s[i])
                A.append("(-")
            else:
                A.append("-")
        A = "".join(A[1:-1])

        def dfs(A, d):
            if not A:
                return None
            A = A.split("(" + d * "-" + ")")
            node = TreeNode(int(A[0]))
            if len(A) == 3:
                node.left = dfs(A[1], d + 1)
                node.right = dfs(A[2], d + 1)
            elif len(A) == 2:
                node.left = dfs(A[1], d + 1)
            return node

        return dfs(A, 1)
