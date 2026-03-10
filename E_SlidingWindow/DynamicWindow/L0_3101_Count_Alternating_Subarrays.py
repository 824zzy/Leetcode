""" https://leetcode.com/problems/count-alternating-subarrays/
sliding window: track start of alternating window, count subarrays ending at each position
"""


class Solution:
    def countAlternatingSubarrays(self, A: List[int]) -> int:
        ans = 0
        i = 0
        for j in range(len(A)):
            if j and A[j] == A[j-1]:
                i = j
            ans += j - i + 1
        return ans
