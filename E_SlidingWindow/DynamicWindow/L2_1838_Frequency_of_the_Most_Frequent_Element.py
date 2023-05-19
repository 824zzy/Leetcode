""" https://leetcode.com/problems/frequency-of-the-most-frequent-element/
maintain the sliding window by making sure the increments always less or equal than k.

the increments in the sliding window is `current_max * window_size - current_sum`.
Note that the current max can be easily found by sorting the array beforehand.
"""
class Solution:
    def maxFrequency(self, A: List[int], k: int) -> int:
        A.sort()
        ans = 1
        i = 0
        sm = 0
        for j in range(len(A)):
            sm += A[j]
            while (j-i+1)*A[j]-sm>k:
                sm -= A[i]
                i += 1
            ans = max(ans, j-i+1)
        return ans