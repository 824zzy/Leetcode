""" https://leetcode.com/problems/next-greater-element-ii/
1. maintain a monotonic decreasing stack
2. linear scan A+A, and use modulo for ans's indexes
"""
class Solution:
    def nextGreaterElements(self, A: List[int]) -> List[int]:
        stk = []
        ans = [-1]*len(A)
        for i, x in enumerate(A+A):
            while stk and A[stk[-1]]<x:
                ii = stk.pop()
                ans[ii] = x
            stk.append(i%len(A))
        return ans