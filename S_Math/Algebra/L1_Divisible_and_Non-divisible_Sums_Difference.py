""" https://leetcode.com/problems/divisible-and-non-divisible-sums-difference/
All the valid integers of num2 are: m, 2m, ... n//m*m
==> m*(1+2+...+n//m)
All the valid integers of num1 are: 1+2+...+sum of nums2
"""


class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        k = n // m
        num2 = m * (k * (k + 1)) // 2
        num1 = (n * (n + 1)) // 2
        return num1 - 2 * num2


# Brute force
class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        a = 0
        b = 0
        for x in range(1, n + 1):
            if x % m == 0:
                b += x
            else:
                a += x
        return a - b
