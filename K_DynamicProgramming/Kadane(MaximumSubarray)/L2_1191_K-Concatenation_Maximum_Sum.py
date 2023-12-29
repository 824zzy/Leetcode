""" https://leetcode.com/problems/k-concatenation-maximum-sum/
Kadane's algorithm + categorization
"""
from header import *

class Solution:
    def kConcatenationMaxSum(self, A: List[int], k: int) -> int:
        MOD = 10**9+7
        # case1: k=1
        ans, cur = -inf, 0
        for x in A:
            cur = max(x, cur+x)
            ans = max(ans, cur)
        # case2: sm*k
        sm = sum(A)
        ans = max(ans, sm*k)
        # case2: k>1
        if k>1:
            pre = max(accumulate(A, initial=0))
            suf = max(accumulate(A[::-1], initial=0))
            sm = max(sm*(k-2), 0)
            ans = max(ans, sm+pre+suf)
        return max(ans, 0)%MOD
    
"""
[1,2]
3
[1,-2,1]
5
[-1,-2]
7
[-5,-2,0,0,3,9,-2,-5,4]
5
[1,2]
1
[-9,13,4,-16,-12,-16,3,-7,5,-16,16,8,-1,-13,15,3]
6
[2,-5,1,0,-2,-2,2]
2
"""