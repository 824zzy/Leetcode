""" https://leetcode.com/problems/maximum-score-using-exactly-k-pairs/
3D DP on subsequence pairing (follow-up of LC 1458 Max Dot Product).

dp(i, j, k) = max score picking exactly k pairs from A[i:] and B[j:] with
strictly increasing indices. Three transitions: skip A[i], skip B[j], or
pair A[i] with B[j] and recurse with k-1. O(n * m * k) time and space.
"""


class Solution:
    def maxScore(self, A: List[int], B: List[int], k: int) -> int:
        @cache
        def dp(i, j, k):
            if k == 0:
                return 0
            if i == len(A) or j == len(B):
                return -inf
            # skip
            ans1 = dp(i + 1, j, k)
            ans2 = dp(i, j + 1, k)
            # choose
            ans3 = A[i] * B[j] + dp(i + 1, j + 1, k - 1)
            return max(ans1, ans2, ans3)
        ans = dp(0, 0, k)
        dp.cache_clear()
        return ans
