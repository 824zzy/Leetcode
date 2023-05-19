""" https://leetcode.com/problems/partition-list/

"""
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        l, r = ListNode(0), ListNode(0)
        rr = r
        ll = l
        while head:
            if head.val<x:
                l.next = ListNode(head.val)
                l = l.next
            else:
                r.next = ListNode(head.val)
                r = r.next
            head = head.next
        l.next = rr.next
        return ll.next