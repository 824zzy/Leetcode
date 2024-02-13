""" https://leetcode.com/problems/majority-element/
Boyer-Moore majority voting algorithm
"""
from header import *

class Solution:
    def majorityElement(self, A: List[int]) -> int:
        cand, freq = None, 0
        for i in range(len(A)):
            if A[i]==cand:
                freq += 1
            else:
                if freq==0:
                    cand = A[i]
                    freq = 1
                else:
                    freq -= 1
        return cand


# suboptimal solution: brute force to find major element by frequency table
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        return [k for k, v in Counter(nums).items() if v>len(nums)//2][0]