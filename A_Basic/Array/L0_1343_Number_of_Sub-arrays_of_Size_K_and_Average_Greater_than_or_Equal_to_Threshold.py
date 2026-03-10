""" https://leetcode.com/problems/number-of-sub-arrays-of-size-k-and-average-greater-than-or-equal-to-threshold/
"""

class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        ans = 0
        slide = arr[:k]
        curr_sum = sum(slide)
        if curr_sum / k >= threshold:
            ans += 1

        for i in range(0, len(arr) - k):
            curr_sum = curr_sum - arr[i] + arr[i + k]
            if curr_sum / k >= threshold:
                ans += 1

        return ans
