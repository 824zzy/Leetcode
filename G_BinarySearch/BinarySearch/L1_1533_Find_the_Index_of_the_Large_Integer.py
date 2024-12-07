""" https://leetcode.com/problems/find-the-index-of-the-large-integer/
binary search
"""


class Solution:
    def getIndex(self, reader) -> int:
        l, r = 0, reader.length() - 1
        while l < r:
            m = (l + r) // 2
            if (r - l) & 1:
                res = reader.compareSub(l, m, m + 1, r)
                if res == 1:
                    r = m
                else:
                    l = m + 1
            else:
                res = reader.compareSub(l, m - 1, m + 1, r)
                if res == 1:
                    r = m
                else:
                    l = m
        return l
