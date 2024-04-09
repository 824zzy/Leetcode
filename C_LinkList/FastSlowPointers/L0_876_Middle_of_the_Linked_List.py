""" https://leetcode.com/problems/middle-of-the-linked-list/
fast slow pointers to find middle node
"""
from header import *


class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        return slow
