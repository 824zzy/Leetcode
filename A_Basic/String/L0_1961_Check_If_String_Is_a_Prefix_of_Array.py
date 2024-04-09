""" https://leetcode.com/problems/check-if-string-is-a-prefix-of-array/
use a prefix string whose length < s to check if it equals to s
"""


class Solution:
    def isPrefixString(self, s: str, A: List[str]) -> bool:
        prefix = ''
        for i in range(len(A)):
            prefix += A[i]
            if prefix == s:
                return True
            elif len(prefix) > len(s):
                return False
        return False
