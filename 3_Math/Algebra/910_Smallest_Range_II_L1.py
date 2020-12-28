class Solution:
    def smallestRangeII(self, A: List[int], K: int) -> int:
        A.sort()
        ans = A[-1]-A[0]
        for i in range(len(A)-1):
            a, b = A[i], A[i+1]
            hi = max(A[-1]-K, a+K)
            lo = min(A[0]+K, b-K)
            ans = min(ans, hi-lo)
        return ans