""" https://leetcode.com/problems/find-the-losers-of-the-circular-game/
simulate based on the rule
"""
from header import *

class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        cnt = [0]*n
        i = 0
        x = 1
        while cnt[i]==0:
            cnt[i] += 1
            i = (i+k*x)%n
            x += 1
        return [i+1 for i in range(len(cnt)) if cnt[i]==0]
        