""" https://leetcode.com/problems/find-the-smallest-divisor-given-a-threshold/
"""
class Solution:
    def smallestDivisor(self, A: List[int], t: int) -> int:
        l, r = 1, max(A)
        while l<r:
            m = (l+r)//2
            if sum(ceil(x/m) for x in A)<t: r = m
            else: l = m+1
        return l