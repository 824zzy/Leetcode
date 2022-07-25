""" https://leetcode.com/problems/sum-of-subarray-minimums/
Instead of finding all the subarrays, the goal is to check the minimums belongs to which subarrays.

1. scan two pass to find next smaller on the left and right by monotonic increasing stack
2. for each A[i] as minimum, find it belongs to which subarrays.

Reference from guan: https://www.youtube.com/watch?v=TZyBPy7iOAw
"""
class Solution:
    def sumSubarrayMins(self, A: List[int]) -> int:
        # next smaller on the right
        R = [len(A)]*len(A)
        stk = []
        for i in range(len(A)):
            while stk and A[stk[-1]]>A[i]:
                R[stk.pop()] = i
            stk.append(i)
        
        # next smaller on the left
        L = [-1]*len(A)
        stk = []
        for i in reversed(range(len(A))):
            while stk and A[stk[-1]]>=A[i]:
                L[stk.pop()] = i
            stk.append(i)
        
        # for each A[i] as minimum, find it belongs to which subarrays.
        ans = 0
        for i, (l, r) in enumerate(zip(L, R)):
            ll = i-l
            rr = r-i
            ans += A[i] * ll * rr
        return ans%(10**9+7)