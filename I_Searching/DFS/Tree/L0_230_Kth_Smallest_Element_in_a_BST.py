""" https://leetcode.com/problems/kth-smallest-element-in-a-bst/
in-order tree traversal
"""
# recursive solution


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stk = []
        node = root
        while stk or node:
            if node:
                stk.append(node)
                node = node.left
            else:
                node = stk.pop()
                k -= 1
                if not k:
                    return node.val
                node = node.right
        return ans

# iterative solution


class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        self.k = k
        self.ans = None

        def dfs(node):
            if not node:
                return
            dfs(node.left)
            self.k -= 1
            if self.k == 0:
                self.ans = node.val
            dfs(node.right)

        dfs(root)
        return self.anse
