""" https://leetcode.com/problems/happy-number/
simulation
"""


class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        while n != 1 and n not in seen:
            seen.add(n)
            sm = 0
            for c in str(n):
                c = int(c)
                sm += c * c
            n = sm
        return n == 1
