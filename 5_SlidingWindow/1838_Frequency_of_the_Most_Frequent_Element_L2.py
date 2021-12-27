""" https://leetcode.com/problems/frequency-of-the-most-frequent-element/
# valid condition: max*size <= k+sum, which is k + sum >= (j - i + 1) * A[j]
"""
class Solution:
    def maxFrequency(self, A: List[int], k: int) -> int:
        A.sort()
        i = 0
        for j in range(len(A)):
            k += A[j]
            if k < A[j]*(j-i+1):
                k -= A[i]
                i += 1
        return j-i+1