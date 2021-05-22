"""
The greedy strategy we adopted is to give priority to the areas 
with small endings and disjoint ones.
"""
class Solution:
    def eraseOverlapIntervals(self, A: List[List[int]]) -> int:
        A = sorted(A, key=lambda x: x[1])
        ans = [A[0]]
        for i in range(1, len(A)):
            if A[i][0]>=ans[-1][1]: ans.append(A[i])
        return len(A)-len(ans)