""" https://leetcode.com/problems/count-dominant-indices/
Reverse the array so the "right subarray" of original index i becomes a prefix
in the reversed array. Track a running sum sm; at reversed index i the average
of the elements to the right of the original position is sm/i. Compare directly.
"""


class Solution:
    def dominantIndices(self, A: List[int]) -> int:
        A.reverse()
        ans = 0
        sm = A[0]
        for i in range(1, len(A)):
            ans += (A[i] > sm / i)
            sm += A[i]
        return ans
