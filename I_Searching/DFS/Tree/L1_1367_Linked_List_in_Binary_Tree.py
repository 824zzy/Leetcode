""" https://leetcode.com/problems/linked-list-in-binary-tree/
traverse tree and check if any path contains the same values of linked list
"""


class Solution:
    def isSubPath(
            self,
            head: Optional[ListNode],
            root: Optional[TreeNode]) -> bool:
        def check(Tnode, Lnode):
            if not Lnode:
                return True
            if not Tnode:
                return False

            if Tnode.val == Lnode.val:
                l = check(Tnode.left, Lnode.next)
                r = check(Tnode.right, Lnode.next)
                return l or r
            else:
                return False

        def dfs(node):
            if not node:
                return False
            if node.val == head.val and check(node, head):
                return True
            l = dfs(node.left)
            r = dfs(node.right)
            return l or r

        return dfs(root)
