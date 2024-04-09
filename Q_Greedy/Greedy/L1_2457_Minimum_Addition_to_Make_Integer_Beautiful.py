""" https://leetcode.com/problems/minimum-addition-to-make-integer-beautiful/
greedily find the minimum target by flooring the i-th digit:
e.g.: for 467, we will check 467, 470, 500
"""


class Solution:
    def makeIntegerBeautiful(self, n: int, t: int) -> int:
        def get(i):
            if i == 0:
                return n
            mod = n // (10**i)
            return (mod + 1) * (10**i)

        for i in range(len(str(n)) + 1):
            x = get(i)
            sm = 0
            for c in str(x):
                sm += int(c)
            if sm <= t:
                return x - n


""" 4 33 0 ?
16
6
467
6
1
1
734504727
10
"""
