""" https://leetcode.com/problems/degree-of-an-array/
hash table + sliding window
"""
from header import *

class Solution:
    def findShortestSubArray(self, A: List[int]) -> int:
        cnt = Counter(A)
        mx = max(cnt.values())
        cand = [k for k, v in cnt.items() if v==mx]
        ans = inf
        for c in cand:
            i, j = 0, len(A)-1
            while A[i]!=c: i += 1
            while A[j]!=c: j -= 1
            ans = min(ans, j-i+1)
        return ans