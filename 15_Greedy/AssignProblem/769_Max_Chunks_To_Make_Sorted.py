""" L1: https://leetcode.com/problems/max-chunks-to-make-sorted/
Iterate the array, if the max(A[0] ~ A[i]) = i,
then we can split the array into two chunks at this index.
"""
# genius solution from lee: https://leetcode.com/problems/max-chunks-to-make-sorted/discuss/113536/Python-Easy-Understood-Solution
class Solution:
    def maxChunksToSorted(self, arr: List[int]) -> int:
        return sum(i == v for i, v in enumerate(accumulate(arr, max)))