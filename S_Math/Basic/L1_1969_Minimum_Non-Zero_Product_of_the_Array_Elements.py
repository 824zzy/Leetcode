""" https://leetcode.com/problems/minimum-non-zero-product-of-the-array-elements/
find the formula by the third example
note that use pow(x, y, z) to calculate (x**y)%z for saving time
"""


class Solution:
    def minNonZeroProduct(self, p: int) -> int:
        return (
            pow(2 ** p - 2, (2 ** p - 2) // 2, 10 ** 9 + 7)
            * (2 ** p - 1)
            % (10 ** 9 + 7)
        )
