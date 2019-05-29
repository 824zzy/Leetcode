""" basic sort idea
"""
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        elements = []
        for l in lists:
            while l:
                elements.append(l.val)
                l = l.next
        elements = sorted(elements)
        
        res = curr = ListNode(0)
        for e in elements:
            t = ListNode(e)
            curr.next = t
            curr = curr.next
        return res.next
        
        

""" better solution using heap
"""
from heapq import heappop, heapify

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        elements = []
        for l in lists:
            while l:
                elements.append(l.val)
                l = l.next
        heapify(elements)
        
        res = curr = ListNode(0)
        while elements:
            t = ListNode(heappop(elements))
            curr.next = t
            curr = t
        return res.next
        
        