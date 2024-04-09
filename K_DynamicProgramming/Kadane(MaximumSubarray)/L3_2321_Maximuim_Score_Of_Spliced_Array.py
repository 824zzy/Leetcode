""" https://leetcode.com/problems/maximum-score-of-spliced-array/submissions/
Need aha moment to understand the problem, learn from lee: https://leetcode.com/problems/maximum-score-of-spliced-array/discuss/2198244/Python-Kadane-Solution
tranlate the problem into: given the difference of two array, find the maximum subarray.

The maximum score of spliced array is the sum of the maximum subarray of the two array plus the corresponding original array.
"""


class Solution:
    def maximumsSplicedArray(self, A: List[int], B: List[int]) -> int:
        def kadane(A, B):
            ans, cur = -inf, 0
            for i in range(len(A)):
                cur = max(A[i] - B[i], cur + A[i] - B[i])
                ans = max(ans, cur)
            return ans + sum(B)

        return max(kadane(A, B), kadane(B, A))
