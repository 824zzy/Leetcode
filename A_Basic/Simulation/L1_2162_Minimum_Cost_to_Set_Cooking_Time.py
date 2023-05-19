""" https://leetcode.com/problems/minimum-cost-to-set-cooking-time/
We have only two choices:
1. Punch minutes and seconds as is,
2. punch minutes - 1 and seconds + 60.

And simulate the process
"""
class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        def cost(A):
            ans = 0
            cur = startAt
            for x in list(A):
                if x==str(cur): ans += pushCost
                else: ans, cur = ans+pushCost+moveCost, x
            return ans
        
        m, s = divmod(targetSeconds, 60)
        cands = []
        if m < 100: cands.append((str(m) + str(s).zfill(2)).lstrip('0')) # remove leading zero of candidates
        if m and s+60 < 100: cands.append((str(m-1) + str(s+60).zfill(2)).lstrip('0'))
        
        ans = inf
        for cand in cands:
            ans = min(ans, cost(cand))
        return ans