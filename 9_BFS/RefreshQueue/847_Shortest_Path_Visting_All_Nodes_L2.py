""" https://leetcode.com/problems/shortest-path-visiting-all-nodes/
"""
class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        queue = [(i, 1 << i) for i in range(len(graph))]
        seen = set(queue)
        ans = 0
        while queue: 
            newq = []
            for i, mask in queue: 
                if mask == (1 << len(graph)) - 1: return ans 
                for ii in graph[i]: 
                    if (ii, mask | (1 << ii)) not in seen: 
                        newq.append((ii, mask | (1 << ii)))
                        seen.add((ii, mask | (1 << ii)))
            queue = newq
            ans += 1