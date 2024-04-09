""" https://leetcode.com/problems/predict-the-winner/
The same as 877 Stone Game
"""
from header import *


class Solution:
    def predictTheWinner(self, A: List[int]) -> bool:
        @cache
        def dp(i, j):
            if i > j:
                return 0
            return max(A[i] - dp(i + 1, j), A[j] - dp(i, j - 1))
        ans = dp(0, len(A) - 1)
        return True if ans >= 0 else False
