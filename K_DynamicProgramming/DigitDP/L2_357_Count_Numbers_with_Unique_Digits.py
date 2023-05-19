""" https://leetcode.com/problems/count-numbers-with-unique-digits/
dp[i] means the count of numbers with unique digits of length i and dp[i] = dp[i-1]*(11-i)
"""
# bottom up solution
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==0: return 1
        elif n==1: return 10
        dp = [0] * (n+1)
        dp[0], dp[1] = 1, 9
        for i in range(2, n+1):
            dp[i] = dp[i-1]*(11-i)
        return sum(dp)

# top down solution
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        @cache
        def dp(i):
            if i==0: return 1
            if i==1: return 9
            return dp(i-1)*(11-i)
        return sum(dp(i) for i in range(n+1))


"""
Or use digit dp template which is way much easier to understand
note that (seen>>d)&1 is way much faster than seen&(1<<d)
"""
class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        if n==0: return 1
        A = list(map(int, str(10**n-1)))
        
        @cache
        def dp(i, isPrefix, isBigger, seen, hasRepeat):
            if i==len(A): return 0
            ans = 0
            for d in range(i==0, 10):
                _isPrefix = isPrefix and d==A[i]
                _isBigger = isBigger or (isPrefix and d>A[i])
                _hasRepeat = hasRepeat | seen&(1<<d)
                _seen = seen|(1<<d)
                if _hasRepeat and not(i==len(A)-1 and _isBigger):
                    ans += 1
                ans += dp(i+1, _isPrefix, _isBigger, _seen, _hasRepeat)
            return ans
                
        return 10**n-dp(0, True, False, 0, False)