""" https://leetcode.com/problems/add-two-numbers-ii/
two pass simulation
"""
from header import *


class Solution:
    def addTwoNumbers(
            self,
            l1: Optional[ListNode],
            l2: Optional[ListNode]) -> Optional[ListNode]:
        A, B = [], []
        while l1:
            A.append(str(l1.val))
            l1 = l1.next
        while l2:
            B.append(str(l2.val))
            l2 = l2.next
        sm = list(str(int(''.join(A)) + int(''.join(B))))
        dummy = node = ListNode(next=0)
        while sm:
            node.next = ListNode(val=int(sm.pop(0)))
            node = node.next
        return dummy.next
