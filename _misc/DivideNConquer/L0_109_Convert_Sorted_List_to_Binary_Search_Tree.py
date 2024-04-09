""" https://leetcode.com/problems/convert-sorted-list-to-binary-search-tree/
1. get all the values in the list
2. Divide and Conquer to build the tree
"""
from header import *


class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        A = []
        while head:
            A.append(head.val)
            head = head.next

        def fn(A):
            if not A:
                return None
            cur = TreeNode(A[len(A) // 2])
            cur.left = fn(A[:len(A) // 2])
            cur.right = fn(A[len(A) // 2 + 1:])
            return cur
        return fn(A)
