""" https://leetcode.com/problems/shortest-path-visiting-all-nodes/
"""
class Solution:
    def shortestPathLength(self, G: List[List[int]]) -> int:
        Q = [(i, 1 << i) for i in range(len(G))]
        seen = set(Q)
        ans = 0
        while Q:
            for _ in range(len(Q)):
                i, mask = Q.pop(0)
                if mask == (1 << len(G)) - 1: return ans 
                for ii in G[i]: 
                    if (ii, mask | (1 << ii)) not in seen: 
                        Q.append((ii, mask | (1 << ii)))
                        seen.add((ii, mask | (1 << ii)))
            ans += 1

class Solution:
    def shortestPathLength(self, G: List[List[int]]) -> int:
        Q = [(i, 1 << i) for i in range(len(G))]
        seen = set(Q)
        ans = 0
        while Q: 
            newq = []
            for i, mask in Q: 
                if mask == (1 << len(G)) - 1: return ans 
                for ii in G[i]: 
                    if (ii, mask | (1 << ii)) not in seen: 
                        newq.append((ii, mask | (1 << ii)))
                        seen.add((ii, mask | (1 << ii)))
            Q = newq
            ans += 1