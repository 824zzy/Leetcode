""" https://leetcode.com/problems/maximum-points-after-collecting-coins-from-all-nodes/
since 0 <= coins[i] <= 10**4 and 2**14=16384, 14 is the upper bound of half_cnt
"""
from header import *
class Solution:
    def maximumPoints(self, edges: List[List[int]], A: List[int], k: int) -> int:
        G = defaultdict(list)
        for i, j in edges:
            G[i].append(j)
            G[j].append(i)
            
        @cache
        def dp(i, p, half_cnt):
            ans1 = (A[i]>>half_cnt) - k
            ans2 = A[i]>>(half_cnt+1)
            for j in G[i]:
                if j!=p:
                    ans1 += dp(j, i, half_cnt)
                    if half_cnt+1<14:
                        ans2 += dp(j, i, half_cnt+1)
            return max(ans1, ans2)
        return dp(0, None, 0)
                    
                    
"""
[[0,1],[1,2],[2,3]]
[10,10,3,3]
5
[[0,1],[0,2]]
[8,4,4]
0
[[1,0],[0,2],[1,3]]
[9,3,8,9]
0
[[0,1],[0,2],[3,2],[0,4]]
[5,6,8,7,4]
7
[[0,1],[2,1]]
[1,6,4]
4
"""