""" https://leetcode.com/problems/find-the-maximum-divisibility-score/
brute force
"""
from header import *

class Solution:
    def maxDivScore(self, nums: List[int], divisors: List[int]) -> int:
        mx = -inf
        ans = 0
        for d in divisors:
            cnt = 0
            for n in nums:
                if n%d==0:
                    cnt += 1
            if cnt>mx or (cnt==mx and d<ans):
                mx = cnt
                ans = d
        return ans
                    