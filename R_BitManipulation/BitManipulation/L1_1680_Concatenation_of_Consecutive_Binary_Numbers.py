""" https://leetcode.com/problems/concatenation-of-consecutive-binary-numbers/
Just brute force

Time complexity: O(n), note that the time complexity of sting slicing depends on the big the slice is.
"""


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        ans = 0
        k = 0
        for x in range(1, n + 1):
            if not x & x - 1:
                k += 1
            ans = ((ans << k) + x) % (10 ** 9 + 7)
        return ans


class Solution:
    def concatenatedBinary(self, n: int) -> int:
        s = ""
        for i in range(1, n + 1):
            s += bin(i)[2:] % (10 ** 9 + 7)
        return int(s, 2)
