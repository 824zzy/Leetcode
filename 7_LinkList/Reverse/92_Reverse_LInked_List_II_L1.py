""" L1: https://leetcode.com/problems/reverse-linked-list-ii/
"""
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        prev = None
        for _ in range(left-1): head, prev = head.next, head
            
        temp_prev, temp_head = prev, head
        for _ in range(left, right+1): head.next, head, prev = prev, head.next, head

        temp_prev.next, temp_head.next = prev, head
        return dummy.next 