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



""" Sorting O(NlogN)
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return sorted(nums)[len(nums)//2]