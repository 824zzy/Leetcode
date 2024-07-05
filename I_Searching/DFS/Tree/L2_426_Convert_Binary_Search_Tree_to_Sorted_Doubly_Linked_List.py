""" https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/
post-order dfs

keep track of head and tail of the linked list
"""
from header import *


class Solution:
    def treeToDoublyList(self, root: "Optional[Node]") -> "Optional[Node]":
        if not root:
            return None

        def dfs(node):
            head = tail = node
            if node.left:
                head, _tail = dfs(node.left)
                _tail.right = node
                node.left = _tail
            if node.right:
                _head, tail = dfs(node.right)
                node.right = _head
                _head.left = node
            return head, tail

        head, tail = dfs(root)
        head.left = tail
        tail.right = head
        return head
