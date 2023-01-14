""" https://leetcode.com/problems/minimum-fuel-cost-to-report-to-the-capital/description/
"""
from header import *

# post order traversal
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        graph = [[] for _ in range(len(roads)+1)]
        for u, v in roads: 
            graph[u].append(v)
            graph[v].append(u)
            
        self.ans = 0 
        def dfs(u, p): 
            ppl = 0 
            for v in graph[u]: 
                if v != p: ppl += dfs(v, u)
            ppl += 1
            if u: 
                self.ans += ceil(ppl/seats)
            return ppl 
        
        dfs(0, -1)
        return self.ans 


# general form
class Solution:
    def minimumFuelCost(self, roads: List[List[int]], seats: int) -> int:
        if not roads: return 0

        G = defaultdict(list)
        for u, v in roads: 
            G[u].append(v)
            G[v].append(u)

        cost = [0]*len(G)
        seen = [False]*len(G)
        seen[0] = True
        def dfs(i):
            if len(G[i])==1 and i!=0: 
                cost[i] = 1
                return 1
            ppl = 1
            for j in G[i]:
                if not seen[j]:
                    seen[j] = True
                    ppl += dfs(j)
            cost[i] = ceil(ppl/seats)
            return ppl
        dfs(0)
        cost[0] = 0
        return sum(cost)