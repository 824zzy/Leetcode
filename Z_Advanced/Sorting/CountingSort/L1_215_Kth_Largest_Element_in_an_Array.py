""" https://leetcode.com/problems/kth-largest-element-in-an-array/
counting sort
"""
from header import *


class Solution:
    def findKthLargest(self, A: List[int], k: int) -> int:
        mn = min(A)
        mx = max(A)
        cnt = [0] * (mx - mn + 1)

        for num in A:
            cnt[num - mn] += 1

        rem = k
        for num in range(len(cnt) - 1, -1, -1):
            rem -= cnt[num]
            if rem <= 0:
                return num + mn
        return -1
