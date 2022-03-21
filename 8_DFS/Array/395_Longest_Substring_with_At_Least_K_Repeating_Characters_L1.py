""" https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
TODO: put it to correct place
Essentially it is a divide and conquer problem: divde the string by characters which frequency lower than k.
"""
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        def dfs(s):
            if len(s)<k: return 0
            freq = Counter(s)
            if min(freq.values()) < k: 
                m = min(freq, key=freq.get)
                return max(dfs(ss) for ss in s.split(m))
            else: return len(s)
            
        return dfs(s)