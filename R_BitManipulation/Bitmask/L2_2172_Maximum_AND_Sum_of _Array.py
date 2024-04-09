""" https://leetcode.com/problems/maximum-and-sum-of-array/
For slots=3, imagine we have a 6-bit mask "XXXXXX".
1. iterate through slots, check any one of continuous two bit is empty
2. use the empty bit as next bit mask, then go to the next state by (A[i]&j)+dp(nextMask, i+1)
"""


class Solution:
    def maximumANDSum(self, A: List[int], slots: int) -> int:
        @cache
        def dp(mask, i):
            if i == len(A):
                return 0
            ans = 0
            # iterate through slots
            for j in range(1, slots + 1):
                # check any one of continuous two bit is empty
                if mask & (1 << 2 * j) == 0 or mask & (1 << 2 * j + 1) == 0:
                    if mask & (1 << 2 * j) == 0:
                        nextMask = mask ^ (1 << 2 * j)
                    else:
                        nextMask = mask ^ (1 << 2 * j + 1)
                    ans = max(ans, (A[i] & j) + dp(nextMask, i + 1))
            return ans

        return dp(0, 0)
