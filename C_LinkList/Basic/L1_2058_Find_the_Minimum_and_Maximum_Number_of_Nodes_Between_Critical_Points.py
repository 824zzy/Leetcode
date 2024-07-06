""" https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/
link list simulation

Time complexity: O(n)
"""

from header import *


# Space complexity: O(1)
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        pre = head
        head = head.next
        left_most = None
        right_most = None
        pre_i = None
        mnD = inf
        i = 1
        while head.next:
            if (pre.val < head.val and head.val > head.next.val) or (
                pre.val > head.val and head.val < head.next.val
            ):
                if left_most == None:
                    left_most = i
                right_most = i
                if pre_i != None:
                    mnD = min(mnD, i - pre_i)
                pre_i = i
            i += 1
            pre = head
            head = head.next
        mnD = mnD if mnD != inf else -1
        mxD = (
            right_most - left_most
            if left_most and right_most and left_most != right_most
            else -1
        )
        return [mnD, mxD]


# Space complexity: O(n)
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        pre = head.val
        cur = head.next
        locs = []
        idx = 0
        while cur and cur.next:
            idx += 1
            if pre < cur.val > cur.next.val or pre > cur.val < cur.next.val:
                locs.append(idx)
            pre = cur.val
            cur = cur.next

        if len(locs) < 2:
            return [-1, -1]
        else:
            return [
                min([locs[i + 1] - locs[i] for i in range(len(locs) - 1)]),
                locs[-1] - locs[0],
            ]


"""
[3,1]
[5,3,1,2,5,1,2]
[1,3,2,2,3,2,2,2,7]
[2,3,3,2]
[2,2,1,3]
"""
