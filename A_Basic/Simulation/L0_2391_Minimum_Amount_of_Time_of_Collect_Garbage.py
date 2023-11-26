""" https://leetcode.com/problems/minimum-amount-of-time-to-collect-garbage/
count different types of garbage and their maximum distance separately
"""
from header import *

class Solution:
    def garbageCollection(self, G: List[str], T: List[int]) -> int:
        T = list(accumulate(T, initial=0))
        def count(t):
            ans = 0
            dis = 0
            for i in range(len(G)):
                x = G[i].count(t)
                if x:
                    ans += x
                    dis = max(dis, T[i])
            return ans+dis
        return count('P')+count('G')+count('M')