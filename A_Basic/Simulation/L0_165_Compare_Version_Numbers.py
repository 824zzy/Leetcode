""" https://leetcode.com/problems/compare-version-numbers/
split the string by dot and use zip longest to greedily find the larger one chunk by one chunk
"""


class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        for x, y in zip_longest(version1.split(
                "."), version2.split("."), fillvalue="0"):
            if int(x) > int(y):
                return 1
            elif int(x) < int(y):
                return -1
        return 0


class Solution:
    def compareVersion(self, x: str, y: str) -> int:
        x = sum([10**(-i) * int(xx) for i, xx in enumerate(x.split('.'))])
        y = sum([10**(-i) * int(yy) for i, yy in enumerate(y.split('.'))])
        if x == y:
            return 0
        elif x < y:
            return -1
        else:
            return 1
