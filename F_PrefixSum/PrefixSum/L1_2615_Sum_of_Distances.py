""" https://leetcode.com/problems/sum-of-distances/
grouping + prefix sum

1. group index by element
2. prefix sum to find cost
"""
from header import *

class Solution:
    def distance(self, A: List[int]) -> List[int]:
        mp = defaultdict(list)
        for i, x in enumerate(A):
            mp[x].append(i)
        
        ans = [0]*len(A)
        for k, v in mp.items():
            pre = list(accumulate(v, initial=0))
            for i, x in enumerate(v):
                l = x*i - pre[i]
                r = (pre[len(v)]-pre[i]) - x*(len(v)-i)
                ans[x] = l+r
        return ans