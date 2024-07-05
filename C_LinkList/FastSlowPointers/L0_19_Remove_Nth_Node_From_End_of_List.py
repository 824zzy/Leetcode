""" https://leetcode.com/problems/remove-nth-node-from-end-of-list/
"""
from header import *


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = fast = slow = ListNode(next=head)
        for _ in range(n):
            fast = fast.next

        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return dummy.next
