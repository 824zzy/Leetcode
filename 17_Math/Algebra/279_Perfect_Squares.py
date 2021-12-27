""" L2: https://leetcode.com/problems/perfect-squares/
https://leetcode-cn.com/problems/perfect-squares/solution/shu-xue-si-ping-fang-he-ding-li-by-bulli-0n06/

Theory:
    1. Lagrange's four-square theorem:  every natural number n can be represented as the sum of four integer squares.
    2. Based on 1., if n!=4**k(8m+7), the natural number n can be represented as at most the sum of three integer squares.
"""
class Solution:
    def numSquares(self, n: int) -> int:
        def is_4square(n):
            while n % 4 == 0:
                n //= 4
            return n % 8 == 7
        
        def is_perfect(n):
            return int(sqrt(n)) ** 2 == n

        if is_perfect(n): return 1
        if is_4square(n): return 4
        for i in range(1, int(sqrt(n)) + 1):
            if is_perfect(n - i * i):
                return 2
        return 3