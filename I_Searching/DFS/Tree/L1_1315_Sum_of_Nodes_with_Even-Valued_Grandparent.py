""" God solution
"""


class Solution:
    def sumEvenGrandparent(self, root, p=1, gp=1) -> int:
        return self.sumEvenGrandparent(root.left, root.val, p) +\
            self.sumEvenGrandparent(root.right, root.val, p) +\
            root.val * (1 - gp % 2) if root else 0


""" Naive Solution
"""


class Solution:
    def sumEvenGrandparent(self, root, p=1, gp=1) -> int:
        self.ans = 0

        def dfs(node):
            if not node:
                return
            if node.val % 2 == 0:
                if node.left:
                    if node.left.left:
                        self.ans += node.left.left.val
                    if node.left.right:
                        self.ans += node.left.right.val
                if node.right:
                    if node.right.left:
                        self.ans += node.right.left.val
                    if node.right.right:
                        self.ans += node.right.right.val
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return self.ans
