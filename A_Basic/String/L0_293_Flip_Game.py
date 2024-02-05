""" https://leetcode.com/problems/flip-game/
linear scan
"""
from header import *

class Solution:
    def generatePossibleNextMoves(self, s: str) -> List[str]:
        ans = []
        for i in range(len(s)-1):
            if s[i]==s[i+1] and s[i]=='+':
                ans.append(s[:i]+'--'+s[i+2:])
        return ans
        