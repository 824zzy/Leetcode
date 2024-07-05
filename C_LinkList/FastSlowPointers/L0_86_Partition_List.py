""" https://leetcode.com/problems/partition-list/
simulation using two dummy nodes
"""
from header import *


class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        a, b = ListNode(), ListNode()
        dummya, dummyb = a, b
        while head:
            if head.val < x:
                a.next = ListNode(head.val)
                a = a.next
            else:
                b.next = ListNode(head.val)
                b = b.next
            head = head.next
        a.next = dummyb.next
        return dummya.next
