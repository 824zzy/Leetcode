""" https://leetcode.com/problems/destroy-sequential-targets/
count x%space
"""
from header import *

class Solution:
    def destroyTargets(self, A: List[int], space: int) -> int:
        cnt = defaultdict(list)
        for x in A:
            cnt[x%space].append(x)
            
        mx = len(max(cnt.values(), key=len))
        ans = inf
        for k, v in cnt.items():
            if len(v)==mx:
                ans = min(ans, min(v))
        return ans