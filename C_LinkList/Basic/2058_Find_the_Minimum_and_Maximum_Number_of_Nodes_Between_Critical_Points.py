""" L2: https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/
find locations by traverse.
"""


class Solution:
    def nodesBetweenCriticalPoints(
            self, head: Optional[ListNode]) -> List[int]:
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
            return [min([locs[i + 1] - locs[i]
                        for i in range(len(locs) - 1)]), locs[-1] - locs[0]]
