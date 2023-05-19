""" https://leetcode.com/problems/non-negative-integers-without-consecutive-ones/
convert n into binary and apply the digit dp template
"""
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