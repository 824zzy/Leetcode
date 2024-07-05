""" https://leetcode.com/problems/maximum-xor-product/
greedily choose the bit that maximizes the xor product
"""


class Solution:
    def maximumXorProduct(self, a: int, b: int, n: int) -> int:
        MOD = 10 ** 9 + 7
        x = 0
        ans = a * b
        for i in range(n - 1, -1, -1):
            y1 = (a ^ x) * (b ^ x)
            xx = x + (1 << i)
            y2 = (a ^ xx) * (b ^ xx)
            if y2 >= y1:
                x = xx
        return (a ^ x) * (b ^ x) % MOD


"""
12
5
4
6
7
5
1
6
3
1
8
0
53449611838892
712958946092406
6
"""
"""
0001

0101

0110
"""
"""
1100

0010

0101
"""
