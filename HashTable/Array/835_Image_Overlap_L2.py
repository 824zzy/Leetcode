from collections import Counter
class Solution:
    def largestOverlap(self, A: List[List[int]], B: List[List[int]]) -> int:
        N = len(A)
        LA  = [i//N*100+i%N for i in range(N**2) if A[i//N][i%N]]
        LB  = [i//N*100+i%N for i in range(N**2) if B[i//N][i%N]]
        c = Counter([a-b for a in A for b in B])
        return max(c.values() or [0])