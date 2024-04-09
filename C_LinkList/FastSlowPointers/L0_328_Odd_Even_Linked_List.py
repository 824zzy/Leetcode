""" https://leetcode.com/problems/odd-even-linked-list/
straight-forward solution using two pointer
"""
from header import *


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        ans = node = ListNode(next=head)
        odd, even = node.next, node.next.next
        pre = even
        while even and even.next:
            odd.next = odd.next.next
            even.next = even.next.next
            even, odd = even.next. odd.next
        odd.next = pre
        return ans.next
