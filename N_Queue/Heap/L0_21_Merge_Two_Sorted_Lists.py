""" https://leetcode.com/problems/merge-two-sorted-lists/
use heap
note that have to have i in heap otherwise it will cause type error
"""


class Solution:
    def mergeTwoLists(
            self,
            l1: Optional[ListNode],
            l2: Optional[ListNode]) -> Optional[ListNode]:
        if not l1:
            return l2
        elif not l2:
            return l1

        ans = node = ListNode(0)
        A = [[l1.val, 0, l1], [l2.val, 1, l2]]
        heapify(A)

        while A:
            v, i, l = heappop(A)
            node.next = ListNode(v)
            node = node.next
            if l.next:
                heappush(A, [l.next.val, i, l.next])
        return ans.next
