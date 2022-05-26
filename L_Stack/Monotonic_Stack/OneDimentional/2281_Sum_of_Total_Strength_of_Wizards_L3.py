""" https://leetcode.com/problems/sum-of-total-strength-of-wizards/
from lee: https://leetcode.com/problems/sum-of-total-strength-of-wizards/discuss/2061985/Python-Solution-O(n)

similar to 907, almost the same as 1856
"""
class Solution:
    def totalStrength(self, A: List[int]) -> int:
        # next small on the right
        R = [len(A)]*len(A)
        stk = []
        for i in range(len(A)):
            while stk and A[stk[-1]]>A[i]:
                R[stk.pop()] = i
            stk.append(i)
        
        # next small on the left
        L = [-1]*len(A)
        stk = []
        for i in reversed(range(len(A))):
            while stk and A[stk[-1]]>=A[i]:
                L[stk.pop()] = i
            stk.append(i)
            
        # for each A[i] as minimum, calculate sum
        ans = 0
        prefix = list(accumulate(accumulate(A), initial=0))
        for i in range(len(A)):
            l, r = L[i], R[i]
            lprefix = prefix[i]-prefix[max(l, 0)]
            rprefix = prefix[r]-prefix[i]
            ln, rn = i-l, r-i
            ans += A[i] * (rprefix*ln-lprefix*rn)
        return ans%(10**9+7)