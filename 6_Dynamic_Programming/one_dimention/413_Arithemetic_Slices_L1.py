class Solution:
    def numberOfArithmeticSlices(self, A: List[int]) -> int:
        dp = [0] * len(A)
        ans = 0
        for i in range(2, len(A)):
            if A[i-1]-A[i-2]==A[i]-A[i-1]: dp[i] =  dp[i-1] + 1
            ans += dp[i]
        return ans