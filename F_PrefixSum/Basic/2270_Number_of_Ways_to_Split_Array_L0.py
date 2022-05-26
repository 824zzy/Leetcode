""" https://leetcode.com/problems/number-of-ways-to-split-array/
linear scan using prefix sum and find valid split by comparing left sum and right sum
"""
class Solution:
    def waysToSplitArray(self, A: List[int]) -> int:
        A = list(accumulate(A))
        ans = 0
        for i in range(len(A)-1):
            if A[i]>=A[-1]-A[i]:
                ans += 1
        return ans