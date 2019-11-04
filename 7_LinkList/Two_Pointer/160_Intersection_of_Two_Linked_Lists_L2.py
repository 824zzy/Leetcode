# Trick of two pointer
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

# Hash set straightforward      
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        seen = set()
        while headA:
            seen.add(headA)
            headA = headA.next
        while headB:
            if headB in seen:
                return headB
            headB = headB.next
        return None