""" basic usage of inplace-linklist
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

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
                
            
"""basic uage of linklist but inefficient
"""       
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        res = dummy = ListNode(-1)
        curr = head
        while curr:
            if curr.val != val:
                dummy.next = ListNode(curr.val)
                dummy = dummy.next
            curr = curr.next
        return res.next
        