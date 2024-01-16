""" https://leetcode.com/problems/find-players-with-zero-or-one-losses/
hash table + counting

use hash table to add new players and count players' losses
"""
from header import *

class Solution:
    def findWinners(self, A: List[List[int]]) -> List[List[int]]:
        cnt = defaultdict(int)
        for i, j in A:
            cnt.setdefault(i, 0)
            cnt[j] += 1
        return [sorted([k for k, v in cnt.items() if v==0]), sorted([k for k, v in cnt.items() if v==1]
)]
