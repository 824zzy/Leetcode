""" L1: template
tmp = cur.next
cur.next = pre
pre = cur
cur = tmp
"""
class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        pre, cur = None, head
        while cur:
            tmp = cur.next
            cur.next = pre
            pre = cur
            cur = tmp
        return pre

# Recursive solution
class Solution(object):
    def reverseList(self, head):
        if not head or not head.next:
            return head
        N = self.reverseList(head.next)
        head.next.next = head.next
        head.next = None
        return N