""" https://leetcode.com/problems/word-break/

"""
class Solution:
    def wordBreak(self, s: str, W: List[str]) -> bool:
        W = set(W)
        @lru_cache(None)
        def dfs(i):
            if i==len(s): return True
            for j in range(i+1, len(s)+1):
                if s[i:j] in W:
                    if dfs(j): return True
            return False
        
        return dfs(0)
    
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for i in range(len(s)):
            for j in range(i+1):
                if s[j:i+1] in wordDict:
                    if j==0 or dp[j-1]:
                        dp[i] = True
        return dp[-1]