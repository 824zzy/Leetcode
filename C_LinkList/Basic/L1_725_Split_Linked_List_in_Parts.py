""" https://leetcode.com/problems/split-linked-list-in-parts/
Linked list simulation
"""
from header import *

class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        l = 0
        node = head
        while node:
            node = node.next
            l += 1
            
        ans = []
        kk = k
        for i in range(k):
            pre = cur = ListNode(next=head)
            n = ceil(l/kk)
            for _ in range(n):
                cur = cur.next
                head = head.next
            cur.next = None
            ans.append(pre.next)
            l -= n
            kk -= 1
        return ans