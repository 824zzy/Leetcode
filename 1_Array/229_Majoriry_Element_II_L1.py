""" Counter hashmap
"""
from collections import Counter
class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        thres = len(nums)//3
        c = Counter(nums)
        ans = []
        for k, v in c.items():
            if v>thres:
                ans.append(k)
        return ans

""" Better method:
counting number through a `set`
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        ans, thres = [], len(nums)//3
        for n in set(nums):
            if nums.count(n)>thres:
                ans.append(n)
        return ans