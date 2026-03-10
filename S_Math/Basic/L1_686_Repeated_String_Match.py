""" https://leetcode.com/problems/repeated-string-match/
key is to find the upper bound of repeat times: len(b)//len(a)+2
"""


class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if set(a) < set(b):
            return -1

        n = 1
        while n < len(b) // len(a) + 2:
            if b in n * a:
                return n
            else:
                n += 1
        return -1
