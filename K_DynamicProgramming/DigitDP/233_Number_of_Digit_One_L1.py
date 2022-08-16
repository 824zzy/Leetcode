""" https://leetcode.com/problems/number-of-digit-one/
"""
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