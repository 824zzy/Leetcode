""" https://leetcode.com/problems/longest-ideal-subsequence/
Longest increasing subsequence - like problem
"""
class Solution:
    def longestIdealString(self, A: str, k: int) -> int:
        A = [ord(x)-97 for x in A]
        dp = [0]*26
        
        for x in A:
            mx = 0
            for y in range(max(x-k, 0), min(x+k+1, 26)):
                mx = max(mx, dp[y])
            dp[x] = mx+1
        return max(dp)


# the top down solution below will Memory Limit Exceeded :(
# Time complexity: O(N*k), (10^5)*25
# Space complexity: O(N*k), (10^5)*25
class Solution:
    def longestIdealString(self, A: str, k: int) -> int:
        A = [ord(x) for x in A]
        @cache
        def dp(i, prev):
            if i==len(A): return 0
            ans = dp(i+1, prev)
            if prev==None or abs(A[i]-prev)<=k: 
                ans = max(ans, 1+dp(i+1, A[i]))
            return ans
        return dp(0, None)