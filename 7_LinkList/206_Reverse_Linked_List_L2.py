""" Pointer & Iterative
1. Reverse Routine:
    while curr:
        prev, prev.next, curr = curr, prev, curr.next
"""
class Solution(object):
    def reverseList(self, head):
        prev, curr = None, head
        while curr:
            prev, prev.next, curr = curr, prev, curr.next
        return prev
        # Another form
        prev, curr = None, head
        while curr:
            temp = curr
            curr = curr.next
            temp.next = prev
            prev = temp
        return prev

""" Recursive solution
"""
class Solution(object):
    def reverseList(self, head):
        if not head or not head.next:
            return head
        N = self.reverseList(head.next)
        head.next.next = head.next
        head.next = None
        return N