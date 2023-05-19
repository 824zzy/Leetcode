""" https://leetcode.com/problems/minimum-cost-to-merge-stones/
similar to burst balloons, nice implementation from ye: https://leetcode.com/problems/minimum-cost-to-merge-stones/discuss/1465680/Python3-dp
"""

from header import *
class Solution:
    def mergeStones(self, A: List[int], l: int) -> int:
        if (len(A)-1)%(l-1): return -1
        A = list(accumulate(A, initial=0))
        
        @cache
        def dp(i, j):
            if j-i<l: return 0
            ans = inf
            for k in range(i+1, j, l-1):
                ans = min(ans, dp(i, k)+dp(k, j))
            if (j-i-1)%(l-1)==0:
                ans += A[j]-A[i]
            return ans
        
        return dp(0, len(A)-1)