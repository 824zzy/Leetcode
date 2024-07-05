""" https://leetcode.com/problems/sort-characters-by-frequency/
the same as 347
"""
from header import *


class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        bucket = [[] for _ in range(len(s))]
        for k, v in cnt.items():
            bucket[-v].append(k)

        ans = []
        for i in range(len(s)):
            for x in bucket[-i - 1]:
                ans.append((i + 1) * x)
        return "".join(ans[::-1])
