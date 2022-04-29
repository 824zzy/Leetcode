""" https://leetcode.com/problems/network-delay-time/
use dijkstra to find minimum delay for all the nodes to receive the signal
"""
class Solution:
    def networkDelayTime(self, A: List[List[int]], n: int, k: int) -> int:
        G = defaultdict(dict)
        for i, j, w in A: G[i][j] = w
            
        pq = [(0, k)]
        seen = {}
        
        while pq:
            cost, i = heappop(pq)
            if i not in seen:
                seen[i] = cost
                for j in G[i]:
                    heappush(pq, (cost+G[i][j], j))
        
        if len(seen)!=n: return -1
        else: return max(seen.values())