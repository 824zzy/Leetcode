class Solution:
    def checkPossibility(self, A: List[int]) -> bool:
        f = True
        for i in range(1, len(A)):
            if A[i]<A[i-1]:
                if not f: return False
                if i==1 or A[i]>=A[i-2]: A[i-1] = A[i]
                else: A[i] = A[i-1]
                f = False
        return True