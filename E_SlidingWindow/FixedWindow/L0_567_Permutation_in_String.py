""" https://leetcode.com/problems/permutation-in-string/
the same as 438.

Use fixed sliding window and hash table to find the permutation of s1 in s2.
Interestingly, the Counter({'b': 1, 'a': 1, 'e': 0}) == Counter({'a': 1, 'b': 1})
"""

from header import *


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        t = Counter(s1)
        cnt = Counter(s2[: len(s1)])
        if cnt == t:
            return True
        for i in range(len(s1), len(s2)):
            cnt[s2[i]] += 1
            cnt[s2[i - len(s1)]] -= 1
            if cnt == t:
                return True
        return False
