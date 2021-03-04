# Trick of two pointer: TIME: O(N), SPACE: O(1)
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        cA, cB = headA, headB
        while cA != cB:
            if not cA: cA = headB
            else: cA = cA.next    
            if not cB: cB = headA
            else: cB = cB.next
        return cA

# Seen set to save linked list A: TIME: O(N), SPACE: O(N)
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        seen = set()
        while headA:
            seen.add(headA)
            headA = headA.next
        while headB:
            if headB in seen: return headB
            headB = headB.next
        return None

# Straight-forward solution
class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        len_A, len_B = 0, 0
        tmp_A, tmp_B = headA, headB
        while tmp_A:
            len_A += 1
            tmp_A = tmp_A.next
        while tmp_B:
            len_B += 1
            tmp_B = tmp_B.next
            
        step_A = max(0, len_A-len_B)
        step_B = max(0, len_B-len_A)
        while step_A:
            headA = headA.next
            step_A -= 1
        while step_B:
            headB = headB.next
            step_B -= 1
        while headA and headB and headA!=headB:
            headA = headA.next
            headB = headB.next
        return headA if headA else None