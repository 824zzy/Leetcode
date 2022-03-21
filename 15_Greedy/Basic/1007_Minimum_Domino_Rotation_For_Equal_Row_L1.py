""" https://leetcode.com/problems/minimum-domino-rotations-for-equal-row/
Heuristics:
1. only need to check A[0] and B[0]
2. only need to check if A[0]/B[0] appears in all the pairs
"""
class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        for x in [A[0],B[0]]:
            if all(x in d for d in zip(A, B)):
                return len(A) - max(A.count(x), B.count(x))
        return -1