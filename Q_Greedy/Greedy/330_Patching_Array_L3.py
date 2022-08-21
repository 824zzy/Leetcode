""" https://leetcode.com/problems/patching-array/
TODO: cnblogs.com/grandyang/p/5165821.html
"""
class Solution:
    def minPatches(self, nums: List[int], n: int) -> int:
        miss, ans, i = 1, 0, 0
        while miss<n:
            if i<len(nums) and nums[i]<=miss:
                miss += nums[i]
                i += 1
            else:
                miss += miss
                ans += 1
        return ans