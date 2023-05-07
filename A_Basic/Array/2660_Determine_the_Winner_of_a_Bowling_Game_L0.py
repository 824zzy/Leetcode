""" https://leetcode.com/problems/determine-the-winner-of-a-bowling-game/
simulation
"""
from header import *

class Solution:
    def isWinner(self, A1: List[int], A2: List[int]) -> int:
        score1 = 0
        score2 = 0
        for i in range(len(A1)):
            if (i>=1 and A1[i-1]==10) or (i>=2 and A1[i-2]==10):
                score1 += 2*A1[i]
            else:
                score1 += A1[i]
        for i in range(len(A2)):
            if (i>=1 and A2[i-1]==10) or (i>=2 and A2[i-2]==10):
                score2 += 2*A2[i]
            else:
                score2 += A2[i]
        if score1>score2: return 1
        elif score1<score2: return 2
        else: return 0