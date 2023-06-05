""" https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/
convert n into binary and apply the digit dp template
"""
from header import *

# new template
class Solution:
    def findIntegers(self, n: int) -> int:
        s = bin(n)[2:]
        
        @cache
        def dp(i, prev_one, is_limit):
            if i==len(s): return 1
            ans = 0
            up = int(s[i]) if is_limit else 1
            for j in range(up+1):
                if not prev_one or (prev_one and j!=1):
                    ans += dp(i+1, j==1, is_limit and j==up)
            return ans
        return dp(0, False, True)


# old template
class Solution:
    def findIntegers(self, n: int) -> int:
        A = list(map(int, bin(n)[2:]))
        
        @cache
        def dp(i, isPrefix, isBigger, hasOne):
            if i==len(A): return 0
            ans = 0
            for d in range(i==0, 2):
                _isPrefix = isPrefix and d==A[i]
                _isBigger = isBigger or (isPrefix and d>A[i])
                if not(hasOne and d==1) and not(i==len(A)-1 and _isBigger):
                    ans += 1+dp(i+1, _isPrefix, _isBigger, d)
            return ans
        # add one for 0
        return dp(0, True, False, False)+1