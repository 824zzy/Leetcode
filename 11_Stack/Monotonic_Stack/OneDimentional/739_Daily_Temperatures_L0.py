""" https://leetcode.com/problems/daily-temperatures/submissions/
use monotonic decreasing stack to keep track of first temperature larger than stack top element.
"""
class Solution:
    def dailyTemperatures(self, A: List[int]) -> List[int]:
        stk = []
        ans = [0] * len(A)
        for i, x in enumerate(A):
            while stk and stk[-1][1]<x:
                ii, _ = stk.pop()
                ans[ii] = i-ii
            stk.append([i, x])
        return ans