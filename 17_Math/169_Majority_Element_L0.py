# Boyer-Moore Vote Algorithm
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        thres = len(nums)//2
        for n in set(nums):
            if nums.count(n)>thres:
                return n