""" https://leetcode.com/problems/word-break-ii/
Compare to backtracking solution, dp solution utilizes sub-states
"""
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        WD = set(wordDict)
        
        @cache
        def dfs(i):
            if i==len(s): return [[]]
            ans = []
            for j in range(i+1, len(s)+1):
                if s[i:j] in WD:
                    ans.extend([s[i:j]]+x for x in dfs(j))
            return ans
        
        return [" ".join(x) for x in dfs(0)]