class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        if K%2==0 or K%5==0:
            return -1
        N = 1
        ans = 1
        while N<float('inf'):
            if N%K==0:
                return ans
            else:
                ans += 1
                N = 10 * N + 1
        return False