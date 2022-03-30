""" https://leetcode.com/problems/sum-of-square-numbers/
variance of 167
"""
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        l, r = 0, round(sqrt(c))
        while l<=r:
            if l**2+r**2<c: l += 1
            elif l**2+r**2>c: r -= 1
            else: return True
        return False