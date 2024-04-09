""" Facebook
"""


class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        return self.checkInc(A) or self.checkDec(A)

    def checkInc(self, A):
        for i in range(1, len(A)):
            if A[i] < A[i - 1]:
                return False
        return True

    def checkDec(self, A):
        for i in range(1, len(A)):
            if A[i] > A[i - 1]:
                return False
        return True
