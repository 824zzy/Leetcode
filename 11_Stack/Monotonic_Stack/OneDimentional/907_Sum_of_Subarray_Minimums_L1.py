""" https://leetcode.com/problems/sum-of-subarray-minimums/
TODO:
"""
class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        stk = []
        ans = []
        for i, x in enumerate(A):
            while stk and A[stk[-1]]>=x: stk.pop()
            if stk:
                j = stk[-1]
                ans.append(ans[j]+x*(i-j))
            else: ans.append(x*(i+1))
            stk.append(i)
        return sum(ans)%(10**9+7)