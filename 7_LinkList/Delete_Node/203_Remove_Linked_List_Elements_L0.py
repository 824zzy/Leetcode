""" basic usage of inplace-linklist
"""
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        dummy = ListNode(-1)
        dummy.next = head
        pre, curr = dummy, dummy.next
        while curr:
            if curr.val == val:
                pre.next = curr.next
            else:
                pre = pre.next
            curr = curr.next
        return dummy.next