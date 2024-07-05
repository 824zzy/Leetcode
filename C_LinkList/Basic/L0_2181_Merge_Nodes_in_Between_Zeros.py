""" https://leetcode.com/problems/merge-nodes-in-between-zeros/
Simulation: simulate the process of merging nodes between zeros.
"""
from header import *


class Solution:
    def mergeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = node = ListNode()
        sm = 0
        head = head.next
        while head:
            if head.val == 0:
                node.next = ListNode(sm)
                node = node.next
                sm = 0
            else:
                sm += head.val
            head = head.next
        return ans.next
