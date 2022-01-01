""" https://leetcode.com/problems/maximum-score-words-formed-by-letters/
for each word, if it can be formed by current letters, one can choose it or ignore it,
otherwise one has to ignore it.
"""
class Solution:
    def maxScoreWords(self, W: List[str], L: List[str], score: List[int]) -> int:
        mp = {chr(i+97): s for i, s in enumerate(score) if s!=0}
        
        def dfs(i, cnt):
            if i==len(W): return 0
            # if all([W[i].count(c)<= cnt.get(c, 0) for c in set(W[i])]):
            if all([v<=cnt.get(k, 0) for k, v in Counter(W[i]).items()]):
                return max(sum(mp[c] for c in W[i])+dfs(i+1, cnt-Counter(W[i])), dfs(i+1, cnt))
            else: return dfs(i+1, cnt)
            
        return dfs(0, Counter(L))