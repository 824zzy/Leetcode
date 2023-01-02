""" https://leetcode.com/problems/count-the-digits-that-divide-a-number/
implementation
"""
class Solution:
    def countDigits(self, n: int) -> int:
        ans = 0
        for c in str(n):
            if n%int(c)==0:
                ans += 1
        return ans