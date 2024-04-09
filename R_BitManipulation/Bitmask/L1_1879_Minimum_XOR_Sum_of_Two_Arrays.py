""" https://leetcode.com/problems/minimum-xor-sum-of-two-arrays/
the same as 2172.
1. iterate through B, check if B[j] is select in bit mask
2. if B[j] is not selected yet, then go to the next state by (A[i]&j)+dp(nxt, i+1)
"""


class Solution:
    def minimumXORSum(self, A: List[int], B: List[int]) -> int:
        n = len(A)

        @cache
        def dp(mask, i):
            if i == n:
                return 0
            ans = inf
            for j in range(n):
                if mask & (1 << j) == 0:
                    nxt = mask ^ (1 << j)
                    ans = min(ans, (A[i] ^ B[j]) + dp(nxt, i + 1))
            return ans

        return dp(0, 0)
