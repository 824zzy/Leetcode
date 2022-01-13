""" https://leetcode.com/problems/non-overlapping-intervals/submissions/
the same as 452: use ma to greedily keep track of maximum end value
"""
class Solution:
    def eraseOverlapIntervals(self, A: List[List[int]]) -> int:
        A.sort(key=lambda x: x[1])
        ans = 0
        ma = -inf
        for i, j in A:
            if ma<=i: ma = j
            else: ans += 1
        return ans