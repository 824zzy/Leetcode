""" L0: simplest sliding window
"""
class Solution:
    def removeElement(self, A: List[int], val: int) -> int:
        i = 0
        for j in range(len(A)):
            if A[j]!=val:
                A[i] = A[j]
                i += 1
        return i