class Solution:
    def numDecodings(self, s: str) -> int:
        if not s:
            return 0
        
        dp = [0] * (len(s)+1)
        dp[0] = 1
        dp[1] = 0 if s[0] = '0' else 1
        
        for i in range(2, len(s)+1):
            if 0 < int(s[i:i-1]) <= 9:
                dp[i] += dp[i-1]
            if 10 <= int(s[i:i-2]) <= 26:
                dp[i] += dp[i-2]
        return dp[-1]
        

""" 231
dp[0] = 1
dp[1] = 1
dp[2] = 2
dp[3] = 2
"""