""" https://leetcode.com/problems/subtree-of-another-tree/
"""


class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        self.ans = False

        def check(node1, node2):
            if not node1 and not node2:
                return True
            elif not node1 or not node2:
                return False
            elif node1.val == node2.val:
                l = check(node1.left, node2.left)
                r = check(node1.right, node2.right)
                return l and r
            else:
                return False

        def dfs(nodeS, nodeT):
            if not nodeS:
                return
            if nodeS.val == nodeT.val and not self.ans:
                self.ans = check(nodeS, nodeT)

            dfs(nodeS.left, nodeT)
            dfs(nodeS.right, nodeT)

        dfs(s, t)
        return self.ans
