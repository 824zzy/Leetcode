""" https://leetcode.com/problems/cinema-seat-allocation/
1. use hash table to find row information
2. iterate over the "slot" to find valid 4-person seats

Categorize into two cases:
1. there are two valid 4-person seats
    1. 2-5
    2. 6-9
2. there is one valid 4-person seat from one of the following three cases:
    1. 2-5
    2. 4-7
    3. 6-9
"""
from header import *


class Solution:
    def maxNumberOfFamilies(
            self, n: int, reservedSeats: List[List[int]]) -> int:
        mp = defaultdict(lambda: [0, 10])
        for r, x in reservedSeats:
            mp[r].append(x)

        ans = (n - len(mp)) * 2
        for k, v in mp.items():
            v.sort()
            for i in range(len(v) - 1):
                l, r = v[i], v[i + 1]
                # two valid answer
                if l < 2 and r > 9:
                    ans += 2
                # one valid answer
                elif l < 2 and r > 5:
                    ans += 1
                elif l < 4 and r > 7:
                    ans += 1
                elif l < 6 and r > 9:
                    ans += 1
        return ans
