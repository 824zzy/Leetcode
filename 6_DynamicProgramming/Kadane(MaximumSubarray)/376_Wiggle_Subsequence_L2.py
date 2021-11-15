""" https://leetcode.com/problems/wiggle-subsequence/
Variance of Kadane's Algorithm, curr is replaced by maxP/maxN
"""
class Solution:
    def wiggleMaxLength(self, A: List[int]) -> int:
        maxP, maxN = 1, 1
        for i in range(1, len(A)):
            if A[i-1]>A[i]:
                maxP = maxN + 1
            elif A[i-1]<A[i]:
                maxN = maxP + 1
        return max(maxP, maxN)