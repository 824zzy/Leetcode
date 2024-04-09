""" https://leetcode.com/problems/count-the-number-of-good-partitions/
1. greedily fine left-most and right-most index of a number
2. sweep line to calculate number of intervals.
3. calculate the partitions
"""
from header import *


class Solution:
    def numberOfGoodPartitions(self, A: List[int]) -> int:
        MOD = 10**9 + 7
        ht = defaultdict(lambda: [inf, -inf])
        for i, x in enumerate(A):
            ht[x][0] = min(i, ht[x][0])
            ht[x][1] = max(i, ht[x][1])

        n = len(A)
        sl = [0] * n
        for _, (i, j) in ht.items():
            sl[i] += 1
            sl[j] -= 1
        cnt = 0
        x = 0
        for i in range(n):
            cnt += sl[i]
            if cnt == 0:
                x += 1
        return pow(2, x - 1, MOD)


"""
[1,2,3,4]
[1,1,1,1]
[1,2,1,3]
[1,2,1,3,4]
[1,5,1,5,6]
"""
