""" https://leetcode.com/problems/broken-calculator/
think reversely change Y to X
"""


class Solution:
    def brokenCalc(self, X: int, Y: int) -> int:
        ans = 0
        while X < Y:
            if Y & 1:
                Y += 1
            else:
                Y //= 2
            ans += 1
        return ans + (X - Y)
