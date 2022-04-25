""" https://leetcode.com/problems/critical-connections-in-a-network/
Tarjan's algorithm
"""
class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        graph = defaultdict(list)
        for u, v in connections: 
            graph[u].append(v)
            graph[v].append(u)
        
        def dfs(x, p, step): 
            """Traverse the graph and collect bridges using Tarjan's algo."""
            disc[x] = low[x] = step
            for xx in graph.get(x, []): 
                if disc[xx] == inf: 
                    step += 1
                    dfs(xx, x, step)
                    low[x] = min(low[x], low[xx])
                    if low[xx] > disc[x]: ans.append([x, xx]) # bridge
                elif xx != p: low[x] = min(low[x], disc[xx])
        
        ans = []
        low = [inf]*n
        disc = [inf]*n
        
        dfs(0, -1, 0)
        return ans 