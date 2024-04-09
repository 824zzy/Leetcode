""" https://leetcode.com/problems/winner-of-the-linked-list-game/
"""
from header import *


class Solution:
    def gameResult(self, head: Optional[ListNode]) -> str:
        res = 0
        while head and head.next:
            if head.val < head.next.val:
                res += 1
            elif head.val > head.next.val:
                res -= 1
            head = head.next.next
        if res > 0:
            return 'Odd'
        elif res < 0:
            return 'Even'
        else:
            return 'Tie'
