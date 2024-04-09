""" https://leetcode.com/problems/number-of-steps-to-reduce-a-number-to-zero/
simple simulation
"""


class Solution:
    def numberOfSteps(self, x: int) -> int:
        ans = 0
        while x:
            ans += 1
            if x & 1:
                x -= 1
            else:
                x //= 2
        return ans

# or simulation by bit manipulation


class Solution:
    def numberOfSteps(self, n: int) -> int:
        ans = 0
        while n != 0:
            ans += 1
            if n & 1:
                n -= 1
            else:
                n >>= 1
        return ans
