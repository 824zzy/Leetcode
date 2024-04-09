""" https://leetcode.com/problems/find-the-winner-of-an-array-game/
simulate the game using two pointers
"""
from header import *


class Solution:
    def getWinner(self, A: List[int], k: int) -> int:
        i = 0
        cnt = 0
        for j in range(1, len(A)):
            if A[j] > A[i]:
                i = j
                cnt = 1
            else:
                cnt += 1
            if cnt == k:
                return A[i]
        return A[i]


"""
[1,2,3]
[2,3,1] 2 1
[3,1,2] 3 1
[3,2,1] 3 2
"""
