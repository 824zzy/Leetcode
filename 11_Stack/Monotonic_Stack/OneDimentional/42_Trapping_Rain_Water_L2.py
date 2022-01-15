""" https://leetcode.com/problems/trapping-rain-water/
"""
class Solution:
    def trap(self, A: List[int]) -> int:
        stk = []
        ans = 0
        for i in range(len(A)):
            while stk and A[stk[-1]]<A[i]:
                btm = A[stk.pop()]
                # if left wall exists
                if stk:
                    w = i-stk[-1]-1
                    h = min(A[i], A[stk[-1]])-btm
                    ans += w*h
            stk.append(i)
        return ans