""" https://leetcode.com/problems/recover-binary-search-tree/
solution from ye: https://leetcode.com/problems/recover-binary-search-tree/discuss/689225/Python3-is-O(1)-space-possible
Intuition: for a valid BST, the output should be in ascending order.
1. iteratively in-order traverse the tree.
2. locate the two nodes where the symmetric order is violated, and swap their values.
"""


class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        stk = []
        node = root
        pre = l = r = None
        while stk or node:
            if node:
                stk.append(node)
                node = node.left
            else:
                node = stk.pop()
                if pre and pre.val > node.val:
                    if not l:
                        l, r = pre, node
                    else:
                        r = node
                pre = node
                node = node.right
        l.val, r.val = r.val, l.val


# naive O(nlogn) solution: inorder traverse twice
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        A = []

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            A.append(node.val)
            dfs(node.right)

        dfs(root)

        A.sort()
        self.idx = 0

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            node.val = A[self.idx]
            self.idx += 1
            dfs(node.right)

        dfs(root)
