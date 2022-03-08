""" https://leetcode.com/problems/merge-k-sorted-lists/
find minimal among lists by heap
note that have to have i in heap otherwise it will cause type error
"""
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        pq = [(x.val, i, x) for i,x in enumerate(lists) if x]
        heapify(pq)
        
        ans = cur = ListNode()
        while pq:
            _, i, x = heappop(pq)
            cur.next = x
            cur = cur.next
            if x.next: heappush(pq, (x.next.val, i, x.next))
        return ans.next