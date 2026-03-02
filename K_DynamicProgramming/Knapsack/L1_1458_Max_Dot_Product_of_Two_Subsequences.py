""" https://leetcode.com/problems/max-dot-product-of-two-subsequences/
0/1 Knapsack on two sequences (base problem for LC 3836).

dp(i, j, k) = max dot product from A[i:] and B[j:], where k is a boolean
indicating whether at least one pair has been selected. Three transitions:
skip A[i], skip B[j], or pair A[i] with B[j]. At base case, return 0 if
at least one pair was picked (k=True), else -inf. O(n * m) time and space.
"""


class Solution:
    def maxDotProduct(self, A: List[int], B: List[int]) -> int:
        @cache
        def dp(i, j, k):
            if i == len(A) or j == len(B):
                return 0 if k else -inf
            # skip
            ans1 = dp(i + 1, j, k)
            ans2 = dp(i, j + 1, k)
            # choose
            ans3 = A[i] * B[j] + dp(i + 1, j + 1, True)
            return max(ans1, ans2, ans3)
        ans = dp(0, 0, False)
        dp.cache_clear()
        return ans
