""" L2: https://leetcode.com/problems/two-best-non-overlapping-events/
"""


class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        E = sorted(events)
        ans = 0
        prefix = 0
        seen = []
        for s, e, v in E:
            heappush(seen, (e, v))
            while seen and seen[0][0] < s:
                ee, ev = heappop(seen)
                prefix = max(prefix, ev)
            ans = max(ans, prefix + v)
        return ans
