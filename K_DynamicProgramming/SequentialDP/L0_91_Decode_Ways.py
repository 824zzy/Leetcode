""" https://leetcode.com/problems/decode-ways/
For bottom up, we need to use extra number at the end of array to record the sum of single and double digit dp result.
"""
from header import *

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
    

# top down without integer conversion
class Solution:
    def numDecodings(self, s: str) -> int:
        @cache
        def dp(i):
            if i==len(s):
                return 1
            if s[i]=='0':
                return 0
            ans = dp(i+1)
            if i+1<len(s):
                if s[i]=='1' and s[i+1] in '0123456789' or s[i]=='2' and s[i+1] in '0123456':
                    ans += dp(i+2)
            return ans
        return dp(0)


# bottom up
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = [0] * (len(s)+2)
        dp[-1] = dp[-2] = 1
        for i in reversed(range(len(s))):
            if 1<=int(s[i])<=9: 
                dp[i] += dp[i+1]
            if 10<=int(s[i:i+2])<=26: 
                dp[i] += dp[i+2]
        return dp[0]