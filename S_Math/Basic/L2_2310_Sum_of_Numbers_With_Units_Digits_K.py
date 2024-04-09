""" https://leetcode.com/problems/sum-of-numbers-with-units-digit-k/
enumerate from 1 to 10 to check if any multiple of k has the same unit as n.
"""


class Solution:
    def minimumNumbers(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        for i in range(1, 11):
            if n >= k * i and n % 10 == (k * i) % 10:
                return i
        return -1


"""
58
9
37
2
0
7
10
1
22
1
2
8
8
8
10
9
"""
