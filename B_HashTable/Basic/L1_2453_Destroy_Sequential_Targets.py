""" https://leetcode.com/problems/destroy-sequential-targets/
Count the frequency of each element modulo space
"""
from header import *


class Solution:
    def destroyTargets(self, A: List[int], space: int) -> int:
        if len(A) == 1:
            return A[0]

        cnt = Counter()
        vals = defaultdict(set)
        for i in range(len(A)):
            cnt[A[i] % space] += 1
            vals[A[i] % space].add(A[i])

        mx = max(cnt.values())
        ans = inf
        for k, v in cnt.items():
            if v == mx:
                ans = min(ans, min(vals[k]))
        return ans


"""
1 3 5 7 8
"""
