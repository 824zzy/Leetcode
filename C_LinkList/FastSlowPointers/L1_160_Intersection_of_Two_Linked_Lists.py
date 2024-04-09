""" https://leetcode.com/problems/intersection-of-two-linked-lists/
"""
# solution from ye:
# https://leetcode.com/problems/intersection-of-two-linked-lists/discuss/642385/JavaPython3-traverse-A-greaterB-and-B-greaterA-at-the-same-time


class Solution:
    def getIntersectionNode(
            self,
            headA: ListNode,
            headB: ListNode) -> ListNode:
        nodeA, nodeB = headA, headB
        while nodeA != nodeB:
            nodeA = nodeA.next if nodeA else headB
            nodeB = nodeB.next if nodeB else headA
        return nodeA

# straight-forward solution


class Solution:
    def getIntersectionNode(
            self,
            A: ListNode,
            B: ListNode) -> Optional[ListNode]:
        la, lb = 0, 0
        tmpa, tmpb = A, B
        while tmpa:
            tmpa = tmpa.next
            la += 1
        while tmpb:
            tmpb = tmpb.next
            lb += 1

        if lb > la:
            A, B = B, A
            lb, la = la, lb
        d = (la - lb)
        for _ in range(d):
            A = A.next

        while A and B:
            if A == B:
                return A
            A = A.next
            B = B.next
        return None
