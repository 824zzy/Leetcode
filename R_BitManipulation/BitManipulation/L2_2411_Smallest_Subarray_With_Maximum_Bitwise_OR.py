""" https://leetcode.com/problems/smallest-subarrays-with-maximum-bitwise-or/
From end to start, find the smallest subarray with maximum bitwise OR by two pointers.
"""
class Solution:
    def smallestSubarrays(self, nums: List[int]) -> List[int]:
        ans = [0]*len(nums)
        seen = [0]*30 
        for i in range(len(nums)-1, -1, -1): 
            for j in range(30): 
                if nums[i] & 1<<j: seen[j] = i 
            ans[i] = max(1, max(seen)-i+1)
        return ans 