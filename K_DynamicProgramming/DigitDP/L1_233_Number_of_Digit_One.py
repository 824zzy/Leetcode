""" https://leetcode.com/problems/number-of-digit-one/
digits dp + counting
"""
from header import *

# new template
class Solution:
    def countDigitOne(self, n: int) -> int:
        high = str(n)
        n = len(high)
        low = str(0).zfill(n)
        
        @cache
        def dfs(i, limit_low, limit_high, cnt):
            if i==n:
                return cnt
            lo = int(low[i]) if limit_low else 0
            hi = int(high[i]) if limit_high else 9
            ans = 0
            for d in range(lo, hi+1):
                ans += dfs(i+1, limit_low and d==lo, limit_high and d==hi, cnt+(d==1))
            return ans
        return dfs(0, True, True, 0)


# old template
class Solution:
    def countDigitOne(self, n: int) -> int:
        A = list(map(int, str(n)))
        
        @cache
        def dp(i, isPrefix, isBigger, cnt):
            if i==len(A): return 0
            ans = 0
            for d in range(i==0, 10):
                _isPrefix = isPrefix and d==A[i]
                _isBigger = isBigger or (isPrefix and d>A[i])
                _cnt = cnt+(d==1)
                if not(i==len(A)-1 and _isBigger):
                    ans += _cnt
                ans += dp(i+1, _isPrefix, _isBigger, _cnt)
            return ans
        
        return dp(0, True, False, 0)