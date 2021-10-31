class Solution:
    def maxProfit(self, A: List[int], f: int) -> int:
        dp_s = [0] * len(A)
        dp_h = [0] * len(A)
        dp_h[0] = -A[0]
        for i in range(1, len(A)):
            dp_s[i] = max(dp_s[i-1], dp_h[i-1]+A[i]-f)
            dp_h[i] = max(dp_h[i-1], dp_s[i-1]-A[i])
        return dp_s[-1]