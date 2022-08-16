""" https://leetcode.com/problems/numbers-with-repeated-digits/
(seen>>d)&1 is way much faster than seen&(1<<d)
"""
class Solution:
    def numDupDigitsAtMostN(self, n: int) -> int:
        A = list(map(int, str(n)))
        
        @cache
        def dp(i, isPrefix, isBigger, seen, hasRepeat):
            if i==len(A): return 0
            ans = 0
            for d in range(i==0, 10):
                _isPrefix = isPrefix and d==A[i]
                _isBigger = isBigger or (isPrefix and d>A[i])
                _hasRepeat = hasRepeat | (seen>>d)&1
                _seen = seen | (1<<d)
                if _hasRepeat and not(i==len(A)-1 and _isBigger):
                    ans += 1
                ans += dp(i+1, _isPrefix, _isBigger, _seen, _hasRepeat)
            return ans
                
        return dp(0, True, False, 0, False)