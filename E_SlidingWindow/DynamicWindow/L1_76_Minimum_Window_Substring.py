""" https://leetcode.com/problems/minimum-window-substring/
1. use a dynamic sliding windows and a Counter to count t's frequency
2. if all Counter's frequencies are more than t, then increase i
"""
from header import *


class Solution:
    def minWindow(self, A: str, t: str) -> str:
        t = Counter(t)
        cnt = Counter()
        i = 0
        ans = (0, len(A) + 1)

        for j in range(len(A)):
            cnt[A[j]] += 1
            while cnt >= t:
                ans = min(ans, (i, j), key=lambda x: (x[1] - x[0]))
                cnt[A[i]] -= 1
                if cnt[A[i]] == 0:
                    cnt.pop(A[i])
                i += 1
        return A[ans[0] : ans[1] + 1] if ans != (0, len(A) + 1) else ""
