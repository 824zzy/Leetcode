class Solution:
    def maxEnvelopes(self, A: List[List[int]]) -> int:
        A = sorted(A, key=lambda x: (x[0], -x[1]))
        dp = [1] * len(A)
        ans = 1
        for i in range(1, len(A)):
            for j in range(i):
                if A[i][1]>A[j][1] and dp[i]<dp[j]+1:
                    dp[i] = dp[j]+1
            if ans<dp[i]: ans = dp[i]
        return ans