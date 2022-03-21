""" https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
The trick is to limit how many distinct characters in the sliding window. 
The limitation can be considered as the criteria to shrink/expand the sliding window:
"""
class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        max_chars = len(Counter(s))
        ans = 0
        for size in range(1, max_chars+1):
            i = 0
            mp = Counter()
            for j in range(len(s)):
                # limit sliding window by number of distinct characters
                while len(mp.values())>size:
                    mp[s[i]] -= 1
                    if mp[s[i]]==0: mp.pop(s[i])
                    i += 1
                mp[s[j]] += 1
                # update ans when all the character frequencies >= k
                if all(v>=k for v in mp.values()):
                    ans = max(ans, sum(mp.values()))
        return ans