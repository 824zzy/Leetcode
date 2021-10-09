""" L1: https://leetcode.com/problems/max-chunks-to-make-sorted/
use seen maximum value as threshold for monotonic stack
"""
class Solution:
    def maxChunksToSorted(self, A: List[int]) -> int:
        s = []
        for i in range(len(A)):
            ma = A[i]
            while s and s[-1]>A[i]:
                ma = max(ma, s.pop())
            s.append(ma)
        return len(s)