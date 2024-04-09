""" https://leetcode.com/problems/min-max-game/
just simulate the min max game, no tricks

Time complexity: O(nlogn)
"""


class Solution:
    def minMaxGame(self, A: List[int]) -> int:
        while len(A) > 1:
            nextA = []
            for idx, i in enumerate(range(0, len(A), 2)):
                if not idx & 1:
                    nextA.append(min(A[i], A[i + 1]))
                else:
                    nextA.append(max(A[i], A[i + 1]))
            A = nextA
        return A[0]
