""" https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/
enumeration + sliding window

1. enumerate on how many distinct characters can be stored in the sliding window. 
2. sliding window template
"""
from header import *

class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        ans = 0
        for l in range(1, len(set(s))+1):
            cnt = Counter()
            i = 0
            for j in range(len(s)):
                cnt[s[j]] += 1
                while len(cnt)>l:
                    cnt[s[i]] -= 1
                    if cnt[s[i]]==0:
                        cnt.pop(s[i])
                    i += 1
                if all(x>=k for x in cnt.values()):
                    ans = max(ans, j-i+1)
        return ans