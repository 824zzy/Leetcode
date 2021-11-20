""" https://leetcode.com/problems/reverse-linked-list/
space O(1): multiple assignmente(lrm=mlr)
space O(n):iteratively pop element by stack
"""
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head: prev, head.next, head = head, prev, head.next
        return prev

# using stack
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stk = []
        node = head
        while node: 
            stk.append(node.val)
            node = node.next
        node = head
        while node:
            node.val = stk.pop()
            node = node.next
        return head