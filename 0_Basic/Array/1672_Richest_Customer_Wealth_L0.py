""" https://leetcode.com/problems/richest-customer-wealth/
find maximum row sum
"""
class Solution:
    def maximumWealth(self, A: List[List[int]]) -> int:
        return max([sum(x) for x in A])