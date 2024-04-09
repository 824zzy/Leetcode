""" https://leetcode.com/problems/merge-intervals
"""


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        for x, y in sorted(intervals):
            if not ans or ans[-1][1] < x:
                ans.append([x, y])  # new interval
            else:
                ans[-1][1] = max(ans[-1][1], y)  # overlapped
        return ans
