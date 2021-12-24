class Solution:
    def numSubarrayProductLessThanK(self, A: List[int], k: int) -> int:
        i, ans = 0, 0
        s = 1
        for j in range(len(A)):
            s *= A[j]
            while s>=k and i<j:
                s /= A[i]
                i += 1
            if s<k:
                ans += j-i+1
        return ans