""" https://leetcode.com/problems/subsets/
Use bit to indicate which element should be included
"""
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = []
        for m in range(1 << len(nums)): 
            seq = []
            for i in range(len(nums)):
                if m & 1 << i: seq.append(nums[i])
            ans.append(seq)
        return ans 