""" https://leetcode.com/problems/total-hamming-distance/
'{0:032b}'.format: a short way to format the integer to a 32 bit binary
"""
class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        ans = 0
        for n in zip(*map('{0:032b}'.format, nums)):
            ans += n.count('1') * n.count('0')
        return ans