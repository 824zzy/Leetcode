""" https://leetcode.com/problems/rotated-digits/
use digit dp template, dp[i] means the count of numbers with unique digits of length i
"""
class Solution:
    def rotatedDigits(self, n: int) -> int:
        A = list(map(int, str(n)))
        rotate = {2, 5, 6, 9}
        non_rotate = {0, 1, 8}
        invalid = {3, 4, 7}
        
        @cache
        def dp(i, isPrefix, isBigger, hasRotate):
            if i==len(A): return 0
            ans = 0
            for d in range(i==0, 10):
                if d in invalid: continue
                _isPrefix = isPrefix and d==A[i]
                _isBigger = isBigger or (isPrefix and d>A[i])
                _hasRotate = hasRotate or d in rotate
                if _hasRotate and not(i==len(A)-1 and _isBigger):
                    ans += 1
                ans += dp(i+1, _isPrefix, _isBigger, _hasRotate)
            return ans
        
        return dp(0, True, False, False)
