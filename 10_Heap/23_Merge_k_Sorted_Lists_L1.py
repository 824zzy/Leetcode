# Facebook
from heapq import *
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        dummy = curr = ListNode(float('inf'))
        heap = []
        while lists:
            for idx, node in enumerate(lists):
                if node:
                    heappush(heap, node.val)
                    lists[idx] = lists[idx].next
                else:
                    lists.remove(node)
        while heap:
            curr.next = ListNode(heappop(heap))
            curr = curr.next
    return dummy.next