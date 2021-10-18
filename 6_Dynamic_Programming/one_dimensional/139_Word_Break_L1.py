class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        for i in range(len(s)):
            for j in range(i+1):
                if s[j:i+1] in wordDict:
                    if j==0 or dp[j-1]:
                        dp[i] = True
        return dp[-1]
        
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * len(s)
        wordDict = set(wordDict)
        dp[0] = s[0] in wordDict
        
        for i in range(1, len(s)):
            for j in range(i+1):
                if s[j:i+1] in wordDict and (j==0 or dp[j-1]): 
                    dp[i] = True
                    break
        
        return dp[-1]