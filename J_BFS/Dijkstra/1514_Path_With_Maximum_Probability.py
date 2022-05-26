""" L1: dijkstra template
"""
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start: int, end: int) -> float:
        e = defaultdict(dict)
        for idx, (i, j) in enumerate(edges):
            e[i][j] = e[j][i] = succProb[idx]
            
        pq = [(-1, start)]
        seen = {}
        while pq:
            prob1, i = heapq.heappop(pq)
            if i not in seen:
                seen[i] = prob1
                for j in e[i]:
                    prob2 = prob1*e[i][j]
                    if j not in seen:
                        heapq.heappush(pq, (prob2, j))
        
        if end not in seen: return 0
        else: return -1*seen[end]