"""L0: sort type greedy"""
class Solution:
    def maximumUnits(self, A: List[List[int]], k: int) -> int:
        ans = 0
        A = sorted(A, key=lambda x:-x[1])
        while A and k>A[0][0]:
            ans += A[0][0]*A[0][1]
            k -= A[0][0]
            A.pop(0)
        return ans + k*A[0][1] if A else ans