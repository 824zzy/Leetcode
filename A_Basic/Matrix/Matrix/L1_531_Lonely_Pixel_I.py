""" https://leetcode.com/problems/lonely-pixel-i/
1. count rows and cols with 'B' to look for lonely pixels
2. check if lonely pixels are existed in rows and cols
"""
from header import *


class Solution:
    def findLonelyPixel(self, A: List[List[str]]) -> int:
        rseen = defaultdict(int)
        cseen = defaultdict(int)
        ans = 0
        for i in range(len(A)):
            for j in range(len(A[0])):
                if A[i][j] == "B":
                    rseen[i] += 1
                    cseen[j] += 1

        for k1, v1 in rseen.items():
            for k2, v2 in cseen.items():
                if v1 == 1 and v2 == 1 and A[k1][k2] == "B":
                    ans += 1
        return ans


"""
[["W","W","B"],["W","B","W"],["B","W","W"]]
[["B","B","B"],["B","B","W"],["B","B","B"]]
[["W","B","W","W"],["W","B","B","W"],["W","W","W","W"]]
"""
