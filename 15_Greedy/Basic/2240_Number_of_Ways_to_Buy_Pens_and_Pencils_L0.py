""" https://leetcode.com/problems/number-of-ways-to-buy-pens-and-pencils/
fix the number of pencils purchased and greedily calculate the number of ways to buy pens
"""
class Solution:
    def waysToBuyPensPencils(self, T: int, A: int, B: int) -> int:
        ans = 0
        for i in range(0, T+1, A):
            ans += (T-i)//B+1
        return ans