""" https://leetcode.com/problems/number-of-wonderful-substrings/
the same as 1542

categorization + bitmask + prefix sum + hash table

1. use bit mask to represent the odd/even times of each letter
2. prefix sum + hash table
presum[j] ^ presum[j]:
    1. 0 means there is no letter occurs odd times
    2. 1 means there is one letter occurs odd times
"""
from header import *


class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        cnt = Counter([0])
        pre = 0
        ans = 0
        for c in word:
            c = ord(c) - 97
            pre ^= 1 << c
            ans += cnt[pre]
            ans += sum(cnt[pre ^ (1 << i)] for i in range(10))
            cnt[pre] += 1
        return ans
