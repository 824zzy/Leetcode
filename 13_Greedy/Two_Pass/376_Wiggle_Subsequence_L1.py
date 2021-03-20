""" TODO: make sure it is two pass type
F records the fluctuations and f as sign flag.
"""
class Solution:
    def wiggleMaxLength(self, A: List[int]) -> int:
        if len(A)==1: return 1
        F = [1] * (len(A)-1)
        for i in range(len(A)-1):
            if A[i]<A[i+1]: F[i] = 1
            elif A[i]>A[i+1]: F[i] = -1
            else: F[i] = 0
                
        ans = abs(F[0])
        f = F[0]
        for i in range(1, len(F)):
            if F[i]!=0:
                if F[i]!=f:
                    f *= -1
                    ans += 1
        return ans+1