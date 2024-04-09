""" https://leetcode.com/problems/jump-game-iii/
"""


class Solution:
    def canReach(self, A: List[int], s: int) -> bool:
        stk = [s]
        A[s] *= -1
        while stk:
            i = stk.pop()
            if A[i] == 0:
                return True
            for j in i + A[i], i - A[i]:
                if 0 <= j < len(A) and A[j] >= 0:
                    stk.append(j)
                    A[j] *= -1
        return False
