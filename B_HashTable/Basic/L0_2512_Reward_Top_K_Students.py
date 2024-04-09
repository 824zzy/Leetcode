""" https://leetcode.com/problems/reward-top-k-students/
implementation problem
"""
from header import *


class Solution:
    def topStudents(
            self,
            P: List[str],
            N: List[str],
            R: List[str],
            IDs: List[int],
            k: int) -> List[int]:
        P, N = set(P), set(N)
        mp = Counter()
        for r, i in zip(R, IDs):
            x = 0
            for w in r.split():
                if w in P:
                    x += 3
                elif w in N:
                    x -= 1
            mp[i] = x
        return [x[0]
                for x in sorted(mp.items(), key=lambda x: (-x[1], x[0]))[:k]]
