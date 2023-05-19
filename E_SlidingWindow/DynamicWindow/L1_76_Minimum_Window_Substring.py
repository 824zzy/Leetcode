""" https://leetcode.com/problems/minimum-window-substring/
1. use a dynamic sliding windows and a Counter to count t's frequency
2. if all Counter's frequencies are less than 0, then increase i
"""
from header import *

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        cnt = Counter(t)
        i = 0
        ans = '*'*(len(s)+1)
        for j in range(len(s)):
            cnt[s[j]] -= 1
            while all(v<=0 for k, v in cnt.items()):
                ans = min(ans, s[i:j+1], key=len)
                if s[i] in cnt:
                    cnt[s[i]] += 1
                i += 1
        return ans if ans != '*'*(len(s)+1) else ''