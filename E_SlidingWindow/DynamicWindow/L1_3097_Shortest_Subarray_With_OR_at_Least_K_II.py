""" https://leetcode.com/problems/shortest-subarray-with-or-at-least-k-ii/
"""

from header import *


class Solution:
    def minimumSubarrayLength(self, A: List[int], k: int) -> int:
        x = 0
        cnt = [0] * 30
        i = 0
        ans = inf
        for j in range(len(A)):
            for ii in range(31):
                if A[j] & (1 << ii):
                    cnt[ii] += 1
                    x |= 1 << ii
            while x >= k and i <= j:
                ans = min(ans, j - i + 1)
                for ii in range(31):
                    if A[i] & (1 << ii):
                        cnt[ii] -= 1
                        if cnt[ii] == 0 and x & (1 << ii):
                            x ^= 1 << ii
                i += 1
        return ans if ans != inf else -1


"""
[1,2,3]
2
[2,1,8]
10
[1,2]
0
"""
