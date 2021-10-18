""" L2: https://leetcode.com/problems/the-time-when-the-network-becomes-idle/
TODO: https://leetcode.com/problems/the-time-when-the-network-becomes-idle/discuss/1524183/Python3-graph
"""
class Solution:
    def networkBecomesIdle(self, edges: List[List[int]], patience: List[int]) -> int:
        graph = {}
        for u, v in edges: 
            graph.setdefault(u, []).append(v)
            graph.setdefault(v, []).append(u)
        
        dist = [-1]*len(graph)
        dist[0] = 0 
        val = 0
        queue = [0]
        while queue: 
            val += 2
            newq = []
            for u in queue: 
                for v in graph[u]: 
                    if dist[v] == -1: 
                        dist[v] = val
                        newq.append(v)
            queue = newq
        
        ans = 0
        for d, p in zip(dist, patience): 
            if p: 
                k = d//p - int(d%p == 0)
                ans = max(ans, d + k*p)
        return ans + 1