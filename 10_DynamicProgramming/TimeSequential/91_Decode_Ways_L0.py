""" https://leetcode.com/problems/decode-ways/
For bottom up, we need to use extra number at the end of array to record the sum of single and double digit dp result.
"""
# top down
class Solution:
    def numDecodings(self, A: str) -> int:
        @cache
        def dp(i):
            if i>=len(A): return 1
            ans = 0
            if 1<=int(A[i])<=9: ans += dp(i+1)
            if 10<=int(A[i:i+2])<=26: ans += dp(i+2)
            return ans
        
        return dp(0)

# bottom up
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0]* (len(s)+1)
        dp[0] = 1
        dp[1] = 0 if s[0]=='0' else 1
        for i in range(2, len(s)+1):
            if 0<int(s[i-1])<=9: dp[i] += dp[i-1]
            if 10<=int(s[i-2:i])<=26: dp[i] += dp[i-2]        
        return dp[-1]