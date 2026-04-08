""" https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/

Single pass, tracking first and previous critical point positions.
- maxDistance = last critical - first critical (always the two endpoints)
- minDistance = min gap between consecutive critical points

Time: O(n), Space: O(1)
"""


class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        pre = head
        head = head.next
        first = None      # position of the first critical point
        prev = None       # position of the most recent critical point
        min_dist = inf
        pos = 1

        while head.next:
            if (pre.val < head.val > head.next.val) or (pre.val > head.val < head.next.val):
                if first is None:
                    first = pos
                if prev is not None:
                    min_dist = min(min_dist, pos - prev)
                prev = pos
            pos += 1
            pre = head
            head = head.next

        if first is None or first == prev:
            return [-1, -1]
        return [min_dist, prev - first]
