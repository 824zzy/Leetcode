""" https://leetcode.com/problems/remove-nodes-from-linked-list/description/
linked list + monotonic stack
"""
from header import *

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(next=head, val=inf)
        node = head
        stk = [ans]
        while node:
            while stk and stk[-1].val<node.val:
                stk.pop()
            stk[-1].next = node
            stk.append(node)
            node = node.next
        return ans.next