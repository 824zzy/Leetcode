""" https://leetcode.com/problems/reach-a-number/
ans target-ans k
6 1 4
10 5 5
15 10 6
"""


class Solution:
    def reachNumber(self, target: int) -> int:
        ans, k = 0, 0
        target = abs(target)
        while ans < target:
            ans += k
            k += 1
        while (ans - target) % 2:
            ans += k
            k += 1
        return k - 1
