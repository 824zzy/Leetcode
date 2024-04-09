""" https://leetcode.com/problems/loud-and-rich/
"""
from header import *


class Solution:
    def loudAndRich(self, A: List[List[int]], quiet: List[int]) -> List[int]:
        e = defaultdict(list)
        n = len(quiet)
        inD = [0] * n
        for i, j in A:
            e[i].append(j)
            inD[j] += 1

        Q = [i for i, x in enumerate(inD) if x == 0]
        ans = list(range(n))
        while Q:
            i = Q.pop(0)
            for j in e[i]:
                if quiet[ans[i]] < quiet[ans[j]]:
                    ans[j] = ans[i]
                inD[j] -= 1
                if not inD[j]:
                    Q.append(j)
        return ans
