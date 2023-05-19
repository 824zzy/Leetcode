""" https://leetcode.com/problems/numbers-at-most-n-given-digit-set/
"""
class Solution:
    def atMostNGivenDigitSet(self, digits: List[str], n: int) -> int:
        digits = list(map(int, digits))
        A = list(map(int, str(n)))
        
        @cache
        def dp(i, isPrefix, isBigger):
            if i==len(A): return 0
            ans = 0
            for d in range(i==0, 10):
                if d not in digits: continue
                _isPrefix = isPrefix and d==A[i]
                _isBigger = isBigger or (isPrefix and d>A[i])
                if not(i==len(A)-1 and _isBigger):
                    ans += 1
                ans += dp(i+1, _isPrefix, _isBigger)
            return ans
        
        return dp(0, True, False)