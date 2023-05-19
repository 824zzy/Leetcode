""" https://leetcode.com/problems/majority-element/
Boyer-Moore majarity voting algorithm
"""
class Solution:
    def majorityElement(self, A: List[int]) -> int:
        cnt, cand = 0, None
        for x in A:
            if cnt==0: cand = x
            if x==cand: cnt += 1
            else: cnt -= 1
        return cand