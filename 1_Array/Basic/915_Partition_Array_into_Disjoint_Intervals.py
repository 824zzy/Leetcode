""" L2: https://leetcode.com/problems/partition-array-into-disjoint-intervals/discuss/955316/Python3-greedy-O(N)
Scan through elements in array A. At any index, check if the current value is smaller than any values seen before.
"""
class Solution:
    def partitionDisjoint(self, nums: List[int]) -> int:
        ans = 0 
        mx = threshold = nums[0]
        for i, x in enumerate(nums): 
            mx = max(mx, x) 
            if x < threshold: # threshold to partition the array
                ans = i 
                threshold = mx
        return ans + 1