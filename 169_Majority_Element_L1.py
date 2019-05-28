""" basic Counter class usage
"""
from collections import Counter
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        thres = len(nums) // 2
        c = dict(Counter(nums))
        for k, v in c.items():
            if v > thres:
                return k



""" basic hashmap usage 
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_dic = {}
        for i in nums:
            if i not in num_dic:
                num_dic[i] = 1
            else:
                num_dic[i] += 1
        for k, v in num_dic.items():
            if v > len(nums) / 2:
                return k
                