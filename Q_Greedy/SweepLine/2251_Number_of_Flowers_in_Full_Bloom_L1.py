""" https://leetcode.com/problems/number-of-flowers-in-full-bloom/
1. use sweep line to find accumulate full blooms
2. use binary search to find the last time point that <= t
"""
from sortedcontainers import SortedDict
class Solution:
    def fullBloomFlowers(self, A: List[List[int]], P: List[int]) -> List[int]:
        sd = SortedDict({0: 0})
        for i, j in A: 
            sd[i] = sd.get(i, 0)+1
            sd[j+1] = sd.get(j+1, 0)-1
        
        cnt = list(accumulate(sd.values()))
        ans = []
        for p in P:
            idx = sd.bisect_right(p)
            ans.append(cnt[idx-1])
        return ans