"""
to place number i only place i at A[i-1], A[i] or A[i+1].
"""
class Solution:
    def isIdealPermutation(self, A: List[int]) -> bool:
        for i, x in enumerate(A):
            if abs(i-x)>1: return False
        return True