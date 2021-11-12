"""L0: https://leetcode.com/problems/reverse-linked-list/
template for reverse a linked list
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head: prev, head.next, head = head, prev, head.next
        return prev