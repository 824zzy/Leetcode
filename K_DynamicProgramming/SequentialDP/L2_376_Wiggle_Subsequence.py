""" https://leetcode.com/problems/wiggle-subsequence/
finding the longest wiggle subsequence at index i by comparing the previous and next element with sign.

Time complexity: O(n)
"""


class Solution:
    def wiggleMaxLength(self, A: List[int]) -> int:
        @cache
        def dp(i, sign):
            if i == len(A) - 1:
                return 1
            if (A[i] - A[i + 1]) * sign < 0:
                return 1 + dp(i + 1, -sign)
            else:
                return dp(i + 1, sign)

        return max(dp(0, 1), dp(0, -1))


# solution 2: variance of kadane's algorithm


class Solution:
    def wiggleMaxLength(self, A: List[int]) -> int:
        maxP, maxN = 1, 1
        for i in range(1, len(A)):
            if A[i - 1] > A[i]:
                maxP = maxN + 1
            elif A[i - 1] < A[i]:
                maxN = maxP + 1
        return max(maxP, maxN)
