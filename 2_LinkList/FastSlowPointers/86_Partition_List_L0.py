class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        l, r = ListNode(-1), ListNode(-1)
        t_l, t_r = l, r
        dummy = head
        while dummy:
            if dummy.val<x:
                t_l.next = ListNode(dummy.val)
                t_l = t_l.next
            else:
                t_r.next = ListNode(dummy.val)
                t_r = t_r.next
            dummy = dummy.next
        t_l.next = r.next
        return l.next