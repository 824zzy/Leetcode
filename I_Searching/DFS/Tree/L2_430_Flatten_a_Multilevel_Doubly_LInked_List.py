""" L2: https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/
https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/discuss/652275/Python3-recursive-and-iterative-solution
"""


class Solution:
    def flatten(self, head: "Node") -> "Node":
        def dfs(node, default=None):
            if not node:
                return default
            node.next = dfs(node.child, dfs(node.next, default))
            if node.next:
                node.next.prev = node
            node.child = None
            return node

        return dfs(head)
