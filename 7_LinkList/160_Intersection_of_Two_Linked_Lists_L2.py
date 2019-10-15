""" Trick of two pointer
"""
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        cA, cB = headA, headB
        while cA != cB:
            if not cA:
                cA = headB
            else:
                cA = cA.next    
            if not cB:
                cB = headA
            else:
                cB = cB.next
        return cA
        