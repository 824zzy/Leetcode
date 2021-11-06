class Solution:
    def numRescueBoats(self, A: List[int], k: int) -> int:
        A = sorted(A)
        l, r = 0, len(A)-1
        ans = 0
        while l<=r:
            if A[l]+A[r]<=k:
                l += 1
            r -= 1
            ans += 1
        return ans