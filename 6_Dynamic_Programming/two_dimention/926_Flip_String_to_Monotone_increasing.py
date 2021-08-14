""" L3: https://leetcode.com/problems/flip-string-to-monotone-increasing/discuss/1394646/Python-DP-is-EASY-From-O(N)-to-O(1)-space-Clean-and-Concise
TODO:
"""
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        @cache
        def dp(i, last):
            if i == len(s): return 0  # Reach to the end
            d = ord(s[i]) - ord('0')
            cand = []
            if d >= last: cand.append(dp(i + 1, d))  # Don't flip
            if 1 - d >= last: cand.append(dp(i + 1, 1 - d) + 1)  # Flip
            return min(cand)  # Choose the minimum number of flips

        return dp(0, 0)
    

class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        n = len(s)
        INF = n  # There are maxmimum N flips we can use to make the string monotone increasing!
        
        dp = [[INF] * 2 for _ in range(n + 1)]
        dp[n][0] = dp[n][1] = 0  # Base case
        for i in range(n - 1, -1, -1):
            for j in range(2):
                d = ord(s[i]) - ord('0')
                if d >= j:
                    dp[i][j] = min(dp[i][j], dp[i + 1][d])  # Don't flip
                if 1 - d >= j:
                    dp[i][j] = min(dp[i][j], dp[i + 1][1 - d] + 1)  # Flip
        return dp[0][0]