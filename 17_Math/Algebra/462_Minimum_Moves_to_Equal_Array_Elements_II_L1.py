# Find the middle element as target
class Solution:
    def minMoves2(self, A: List[int]) -> int:
        t = sorted(A)[len(A)//2]
        ans = sum([abs(t-a) for a in A])
        return ans