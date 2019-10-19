""" basic Counter class usage: O(N)
Essentially it is Hashmap
"""
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        thres = len(nums) // 2
        c = dict(Counter(nums))
        for k, v in c.items():
            if v > thres:
                return k

""" Better method:
counting number through a `set`
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        thres = len(nums)//2
        for n in set(nums):
            if nums.count(n)>thres:
                return n