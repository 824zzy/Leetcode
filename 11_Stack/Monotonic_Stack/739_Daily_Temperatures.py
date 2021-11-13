""" L1: https://leetcode.com/problems/daily-temperatures/submissions/
use monotonic decreasing stack to keep track of first temperature larger than stack top element.
"""
class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        stk = []
        ans = [0] * len(T)
        for i, t in enumerate(T):
            while stk and T[stk[-1]]<t:
                ii = stk.pop()
                ans[ii] = i-ii
            stk.append(i)
        return ans