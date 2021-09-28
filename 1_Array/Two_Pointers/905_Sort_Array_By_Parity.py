""" L0
simple two pointer usage
"""
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        even, odd = 0, len(A)-1
        while even<odd:
            if A[even]%2==1 and A[odd]%2==0:
                A[even], A[odd] = A[odd], A[even]
            elif A[even]%2==0: even += 1
            elif A[even]%2==1: odd -= 1
        return A