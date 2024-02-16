""" https://leetcode.com/problems/minimum-time-to-revert-word-to-initial-state-ii/
"""
from header import *

class Solution:
    def minimumTimeToInitialState(self, s: str, k: int) -> int:
        def z_function(s):
            n = len(s)
            z = [0] * n
            l, r = 0, 0
            for i in range(1, n):
                if i <= r:
                    z[i] = min(r - i + 1, z[i - l])
                while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                    z[i] += 1
                if i + z[i] - 1 > r:
                    l, r = i, i + z[i] - 1
            return z
        z = z_function(s)
        
        for i, x in enumerate(z):
            if i%k!=0: continue
            if len(s)-i==x:
                return i//k
        return ceil(len(s)/k)