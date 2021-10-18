""" L1
find maximum length by recording up&down states.
"""
class Solution:
    def maxTurbulenceSize(self, A: List[int]) -> int:
        dp = [1]*len(A)
        up = down = 1
        for i in range(1, len(A)):
            if A[i]>A[i-1]:
                up, down = down+1, 1
                dp[i] = up
            elif A[i]<A[i-1]:
                up, down = 1, up+1
                dp[i] = down
            else: up = down = 1
        return max(dp)