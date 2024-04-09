""" https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/description/
Post order traversal along with the fuel and rep count.
Note that we need to record the answer in the root node.
"""
from header import *

# post order traversal


class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        G = defaultdict(list)
        for i, j in roads:
            G[i].append(j)
            G[j].append(i)
        self.ans = 0

        def dfs(i, p):
            fuel = 0
            rep = 1
            for j in G[i]:
                if j != p:
                    _rep, _fuel = dfs(j, i)
                    fuel += _fuel
                    rep += _rep
            if i == 0:
                self.ans = fuel
            return rep, fuel + ceil(rep / seats)

        dfs(0, None)
        return self.ans
